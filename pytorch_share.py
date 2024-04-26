import time

import torch
import torch.nn as nn
import torch.multiprocessing as mp

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

def worker(rank, model):
    # 将模型加载到指定的 GPU 上
    # 使用模型进行推理
    input_data = torch.randn(1, 10)
    output = model(input_data)
    time.sleep(100)
    print(f"Process {rank}, Output: {output}")

if __name__ == '__main__':
    # mp.set_start_method('spawn')
    # 创建模型实例
    model = Model()
    # model.cuda()

    # 多进程共享 GPU 模型实例
    processes = []
    for i in range(5):
        p = mp.Process(target=worker, args=(i, model))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()