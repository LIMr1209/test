import multiprocessing
import time


def add(num, value, lock):
    try:
        lock.acquire()
        print('add{0}:num={1}'.format(value, num.value))
        for i in range(0, 2):
            num.value += value
            print('add{0}:num={1}'.format(value, num.value))
            print('-------add{} add end-------'.format(value))

            time.sleep(1)
    except Exception as err:
        raise err
    finally:
        lock.release()


def change(arr):
    for i in range(len(arr)):
        arr[i] = 1


# if __name__ == '__main__':
    # lock = multiprocessing.Lock()
    # num = multiprocessing.Value('i', 0)
    # arr = multiprocessing.Array('i', range(10))
    #
    # print(arr[:])
    # p1 = multiprocessing.Process(target=add, args=(num, 1, lock))
    # p3 = multiprocessing.Process(target=add, args=(num, 3, lock))
    # p = multiprocessing.Process(target=change, args=(arr,))
    # p3.start()
    # p1.start()
    # p.start()
    # p.join()
    # print(arr[:])
    #
    # print('main end...')

# 先执行进程p3并加锁，p3执行过程中进程p执行，因为p没有调用锁且使用了join()方法，阻塞了其它进程，只有当p执行完成后
# p3才会继续执行，p3执行完成后，p1抢到锁并执行
#
# p1、p3 都对共享内存num 进行累加操作，所以num的值一直在增加
# p 对 arr 共享数组中的每个值进行了重新赋值的操作，所以当P进程执行完成后，arr数组中的值均发生了变化
#
# 由上例可以看出：
# 1、进程锁只对调用它的进程起锁的作用，未调用该锁的进程不受影响
# 2、在未调用进程锁的进程中使用 join() 方法会阻塞已调用进程锁的进程

