# Python program raising
# exceptions in a python
# thread

import threading
import ctypes
import time
from concurrent.futures.thread import ThreadPoolExecutor


# https://stackoverflow.com/questions/65089503/raising-exceptions-in-a-thread
# class thread_with_exception(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name
#
#     def run(self):
#
#         # target function of the thread class
#         try:
#             while True:
#                 print('running ' + self.name)
#         finally:
#             print('ended')
#
#     def get_id(self):
#         # returns id of the respective thread
#         if hasattr(self, '_thread_id'):
#             return self._thread_id
#         for id, thread in threading._active.items():
#             if thread is self:
#                 return id
#
#     def raise_exception(self):
#         thread_id = self.get_id()
#         res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id),
#                                                          ctypes.py_object(SystemExit))
#         if res > 1:
#             ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
#             print('Exception raise failure')
#
#
# t1 = thread_with_exception('Thread 1')
# t1.start()
# time.sleep(2)
# t1.raise_exception()
# t1.join()

thread_ids = []

def task(name):
    global thread_id
    print(threading.current_thread().ident)
    thread_ids.append(threading.current_thread().ident)
    print("开始执行任务:", name)
    time.sleep(2)
    print("任务结束:", name)
    return name
#
#
with ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务给线程池执行
    future1 = executor.submit(task, 'A')
    future2 = executor.submit(task, 'B')
    time.sleep(1)
    for i in thread_ids:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(i),
                                                   ctypes.py_object(SystemExit))

    # # 获取任务的执行结果
    # result1 = future1.result()
    # result2 = future2.result()
