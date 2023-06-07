import multiprocessing
import signal

def worker(name):
    print(f"Worker {name} started")
    while True:
        pass

def on_exit(signum, frame):
    print("Ctrl-C received. Exiting...")
    pool.terminate()
    pool.join()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, on_exit)

    pool = multiprocessing.Pool(processes=4)
    for i in range(4):
        pool.apply_async(worker, args=(i,))

    pool.close()
    pool.join()
