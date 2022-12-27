import os

import torch
# from torch.distributed import *
tensor_list = [torch.zeros(2, dtype=torch.int64) for _ in range(2)]
# tensor_list =1
print(tensor_list)
rank=2
tensor = torch.arange(2, dtype=torch.int64) + 1 + 2 * rank
print(tensor)
print(torch.arange(2, dtype=torch.int64))