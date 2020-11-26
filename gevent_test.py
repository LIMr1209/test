import gevent
from gevent import monkey

monkey.patch_socket()


def f1(i):
    print('this is ' + str(i))
    gevent.sleep(3)


def upload():
    page = 1
    is_end = False
    while not is_end:
        evts = []
        for i in range(5):
            evt = gevent.spawn(
                f1, i,
            )
            evts.append(evt)
        jobs = gevent.joinall(evts)
        print("current page %s: \n" % page)
        page += 1
        if page == 100:
            is_end = True
    print("is over execute count")


upload()
