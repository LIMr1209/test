from multiprocessing import shared_memory
from time import sleep


class ShmExampleWorkerAPP:
    def __init__(self, name):
        self.shl = shared_memory.ShareableList(None, name=name)
        self.round_counter = 0

    def __del__(self):
        self.shl.shm.close()

    def run(self):
        while True:
            r, data = self.shl[0], self.shl[1]
            if r != self.round_counter:
                print(data.upper())
                self.round_counter = r
            sleep(0.5)


if __name__ == '__main__':
    shm_key = input('place input shm key:')
    app = ShmExampleWorkerAPP(shm_key)
    app.run()