# -*- coding: utf-8 -*-

import os
import random

image_dir = '/home/deepsi/Polyp_Detector/darknet/data/Roboflow_Data/'

train_file = '/home/deepsi/Polyp_Detector/darknet/data/Roboflow_Data/train.txt'
test_file = '/home/deepsi/Polyp_Detector/darknet/data/Roboflow_Data/test.txt'


split_ratio = 0.8

# Collect all image file paths
image_extensions = ['.jpg', '.jpeg', '.png']
images = [os.path.join(image_dir, f) for f in os.listdir(image_dir)
          if os.path.splitext(f)[1].lower() in image_extensions]

# Shuffle for randomness
random.shuffle(images)

# Split into train and test
split_index = int(len(images) * split_ratio)
train_images = images[:split_index]
test_images = images[split_index:]

# Save to train.txt and test.txt
with open(train_file, 'w') as f:
    for item in train_images:
        f.write(item + '\n')

with open(test_file, 'w') as f:
    for item in test_images:
        f.write(item + '\n')

print(f'Total images: {len(images)}')
print(f'Training set: {len(train_images)}')
print(f'Test set: {len(test_images)}')
print(f'Train.txt and test.txt saved!')