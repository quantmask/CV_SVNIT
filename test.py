import torch
import argparse
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.utils import save_image as imwrite
import os
import time
import re
from torchvision import transforms
from test_dataset import dehaze_test_dataset
from model import final_net

parser = argparse.ArgumentParser(description='Shadow')
parser.add_argument('--test_dir', type=str, default='../ShadowDataset/test')
parser.add_argument('--output_dir', type=str, default='../results/')
parser.add_argument('--test_batch_size', help='Set the testing batch size', default=1, type=int)
args = parser.parse_args()

output_dir = args.output_dir
if not os.path.exists(output_dir):
    os.makedirs(output_dir, exist_ok=True)

test_dir = args.test_dir
test_batch_size = args.test_batch_size

test_dataset = dehaze_test_dataset(test_dir)
test_loader = DataLoader(dataset=test_dataset, batch_size=test_batch_size, shuffle=False, num_workers=0)

device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

model = final_net()
weight_dir = '..\weights'
removal_path = os.path.join(weight_dir, 'shadowremoval.pkl')
enhancement_path = os.path.join(weight_dir, 'refinement.pkl')

try:
    model.remove_model.load_state_dict(torch.load(removal_path, map_location=device), strict=True)
    print('loading removal_model success')
except Exception as e:
    print(f'loading removal_model error: {e}')

try:
    model.enhancement_model.load_state_dict(torch.load(enhancement_path, map_location=device), strict=True)
    print('loading enhancement model success')
except Exception as e:
    print(f'loading enhancement model error: {e}')

model = model.to(device)

total_time = 0
with torch.no_grad():
    model.eval()

    start = time.time()
    for batch_idx, (input, name) in enumerate(test_loader):
        print(name[0])

        input = input.to(device)
        frame_out = model(input)

        name = re.findall("\d+", name[0])

        imwrite(frame_out, os.path.join(output_dir, f"{name[0]}.png"))

print("Inference complete!")
