from multiprocessing import managers


class ShmExampleMainAPP:
    def __init__(self):
        self.smm = managers.SharedMemoryManager()
        self.smm.start()
        self.shl = self.smm.ShareableList([0, ''])
        self.round_counter = 0
        print(self.shl.shm.name)

    def handle_input(self):
        data = input("place input data:")
        self.shl[0] = self.round_counter + 1
        self.shl[1] = data
        self.round_counter += 1

    def run(self):
        while True:
            try:
                self.handle_input()
            except KeyboardInterrupt:
                break
        self.smm.shutdown()


if __name__ == '__main__':
    app = ShmExampleMainAPP()
    app.run()