from threading import Thread, Lock
import time

number = 0
# 加锁
lock = Lock()


def target():
    global number
    for _ in range(1000000):
        # with lock:
        #     number += 1
        lock.acquire()
        number += 1
        lock.release()


start = time.perf_counter()
thread_01 = Thread(target=target)
thread_02 = Thread(target=target)
thread_01.start()
thread_02.start()

thread_01.join()
thread_02.join()
end = time.perf_counter()
print(end - start)
print(number)

# 使用 celery 默认 prefork
# daemonic processes are not allowed to have children
# 使用 from billiard.context import Process 可以解决创建多进程，但无法使用共享变量
# 使用 celery 协程 gevent  打补丁 出现进程错乱
# Resource temporarily unavailable

# 使用threads blender defunct