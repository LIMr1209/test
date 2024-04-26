import copy
import multiprocessing

from celery import Task, Celery
from kombu import Queue, Exchange
import threading

broker_url = "amqp://guest@localhost//"
result_backend = "redis://localhost"

conf = {
    "broker_url": broker_url,
    "result_backend": result_backend,
    "result_expires": 10,
    "task_serializer": "json",
    "result_serializer": "json",
    "accept_content": ['json'],
    "timezone": 'Asia/Shanghai',
    "worker_concurrency": 1,
    # "enable_utc": True,
    "task_create_missing_queues": True,
    "worker_prefetch_multiplier": 1,
    "broker_connection_retry_on_startup": True,
    "broker_connection_max_retries": None,
    "worker_max_tasks_per_child": 2,
    "worker_pool": "solo",
}


class CeleryBase(Celery):

    def gen_task_name(self, name, module):
        return self.main + "." + name


def keep_active():
    while True: pass


def child(app_name):
    print(f"child {app_name} started")
    app = CeleryBase("async_queue_" + app_name)
    app_conf = copy.deepcopy(conf)
    app_conf["task_queues"] = (
        Queue("async_queue_" + app_name, Exchange("async_queue_" + app_name, type="direct"),
              routing_key="async_queue_" + app_name + ".#"),
    )
    app.config_from_object(app_conf)
    args = ['worker', '--loglevel=INFO', "-n async_queue_" + app_name]
    app.worker_main(args)


def worker(name):
    print(f"parent {name} started")
    for i in range(2):
        process = multiprocessing.Process(target=child, args=(f"child_{str(i)}",), daemon=True)
        process.start()
    p1 = threading.Thread(target=keep_active, daemon=True)
    p1.start()
    p1.join()
    # while True:
    #     pass


if __name__ == '__main__':
    processes = []
    for i in range(1):
        process = multiprocessing.Process(target=worker, args=(f"parent_{str(i)}",))
        process.start()
        processes.append(process)
    try:
        while True:
            pass
    except KeyboardInterrupt:
        for i in processes:
            print(i)
            i.kill()
