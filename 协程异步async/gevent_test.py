import gevent
from gevent import monkey

monkey.patch_socket()


def f1(i):
    gevent.sleep(5)
    print('this is ' + str(i))


def upload():
    page = 1
    is_end = False
    while not is_end:
        evts = []
        for i in range(100):
            evt = gevent.spawn(
                f1, i,
            )
            evts.append(evt)
        jobs = gevent.joinall(evts)
        print("current page %s: \n" % page)
        page += 1
        if page == 2:
            is_end = True
    print("is over execute count")


upload()
