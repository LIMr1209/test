from multiprocessing import Process
from multiprocessing import Queue  # 进程间通信Queue，两者不要混淆


# from queue import Queue  # 线程间通信queue.Queue，两者不要混淆

def p_put(q, *args):
    q.put(args)
    print('Has put %s' % args)


def p_get(q, *args):
    print('%s wait to get...' % args)

    print(q.get())
    print('%s got it' % args)


# if __name__ == "__main__":
#     q = Queue()
#     p1 = Process(target=p_put, args=(q, 'p1',))
#     p2 = Process(target=p_get, args=(q, 'p2',))
#     p1.start()
#     p2.start()

# 在线程间通信的时候可以使用Queue模块完成，进程间通信也可以通过Queue完成，
# 但是此Queue并非线程的Queue，进程间通信Queue是将数据 pickle 后传给另一个进程的 Queue，
# 用于父进程与子进程之间的通信或同一父进程的子进程之间通信；

# 使用Queue线程间通信：
# #导入线程相关模块
# import threading
# import queue
#
# q = queue.Queue()


# 使用Queue进程间通信，适用于多个进程之间通信：
# # 导入进程相关模块
# from multiprocessing import Process
# from multiprocessing import Queue
#
# q = Queue()


# 使用Pipe进程间通信，适用于两个进程之间通信（一对一）：
# # 导入进程相关模块
# from multiprocessing import Process
# from multiprocessing import Pipe
#
# pipe = Pipe()

# Pipe的读写效率要高于Queue。
# Pipe常用于两个进程，两个进程分别位于管道的两端 * Pipe方法返回（conn1,conn2）代表一个管道的两个端，Pipe方法有duplex参数，默认为True，即全双工模式，若为FALSE，conn1只负责接收信息，conn2负责发送,Pipe同样也包含两个方法：
#
# send() : 发送信息;
#
# recv() : 接收信息;

from multiprocessing import Process
from multiprocessing import Pipe
import os, time, random


# 写数据进程执行的代码
def proc_send(pipe, urls):
    # print 'Process is write....'
    for url in urls:
        print('Process is send :%s' % url)
        pipe.send(url)
        time.sleep(random.random())


# 读数据进程的代码
def proc_recv(pipe):
    while True:
        print('Process rev:%s' % pipe.recv())
        time.sleep(random.random())


if __name__ == '__main__':
    # 父进程创建pipe，并传给各个子进程
    pipe = Pipe()
    p1 = Process(target=proc_send, args=(pipe[0], ['url_' + str(i) for i in range(10)]))
    p2 = Process(target=proc_recv, args=(pipe[1],))
    # 启动子进程，写入
    p1.start()
    p2.start()

    p1.join()
    p2.terminate()  # 当 p1 join 执行完成 杀死 p2 进程
    print("mian")
