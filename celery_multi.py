import copy
import multiprocessing
import os
import random
import signal
import sys
import concurrent.futures
import time

from celery import Task, Celery, states
from celery.contrib.abortable import AbortableTask
from celery.contrib import rdb
from kombu import Queue, Exchange
from celery.exceptions import SoftTimeLimitExceeded

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
    # "worker_pool": "solo",
}


class CeleryBase(Celery):

    def gen_task_name(self, name, module):
        return self.main + "." + name


class TaskBase(AbortableTask):
    def on_success(self, retval, task_id, args, kwargs):
        self.update_state(
            state=states.SUCCESS,
            meta={'progress': 100}
        )

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.update_state(
            state=states.FAILURE,
            meta={'progress': 0}
        )

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        self.update_state(
            state=states.RETRY,
            meta={'progress': 0}
        )
def resister(app_name, func):
    app = CeleryBase("async_queue_" + app_name)
    app_conf = copy.deepcopy(conf)
    app_conf["task_queues"] = (
        Queue("async_queue_" + app_name, Exchange("async_queue_" + app_name, type="direct"),
              routing_key="async_queue_" + app_name + ".#"),
    )
    a = random.randint(1, 100)
    app.meta = {"111": a}
    app.config_from_object(app_conf)
    app.task(func, bind=True, base=TaskBase, soft_time_limit=4)
    # app.register_task(task_obj)
    args = ['worker', '--loglevel=INFO', "-n async_queue_" + app_name]
    app.worker_main(args)


def func(self):
    try:
        print(self.app.meta)
        # rdb.set_trace()
        for i in range(10):
            time.sleep(5)
            if self.is_aborted():
                break
            self.update_state(
                state='PROGRESS',
                meta={'progress': round(i/10, 2)*100}
            )
            print(self.is_aborted())
            print(f"sleeping {str(i)}/10")
        return self.app.meta
    except SoftTimeLimitExceeded:
        print(1111)


def error(e):
    print(str(e))


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    for i in range(2):
        pool.apply_async(func=resister, args=("test" + str(i), func), error_callback=error)
    pool.close()
    try:
        pool.join()
    except KeyboardInterrupt:
        time.sleep(10)
