import time

from celery import Celery
from celery.contrib.abortable import AbortableAsyncResult

app = Celery(broker="amqp://guest@localhost//", backend="redis://localhost")
s = app.send_task("async_queue_test0.func", queue="async_queue_test0", soft_time_limit=2)
print(str(s))
time.sleep(5)

task_id = str(s)
# # app.control.revoke(task_id, terminate=True, signal='SIGKILL')
abortable_task = AbortableAsyncResult(task_id)
# # abortable_task.abort()
while True:
    time.sleep(1)
    print(abortable_task.state)
    print(abortable_task.result)

