# Endoscopy Polyp Detector using YOLOv4 Darknet

This is a demonstration of a polyp detection model inspired by work I’ve done professionally for real time endoscopy feeds using the YOLOV4 DARKNET.

## 🚀 Quick Start

### Prerequisites
- Linux/Ubuntu system
- CUDA-capable GPU (recommended)
- OpenCV
- CUDA and cuDNN (for GPU acceleration)

### Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Deepsi11/Endoscopy_Polyp_Detector_Yolov4_Darknet.git
cd Endoscopy_Polyp_Detector_Yolov4_Darknet
```

2. **Build Darknet:**
```bash
make
```

3. **Download pre-trained weights (if not included):**
```bash
# Download YOLOv4 pre-trained weights
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137
```

## 🎯 Usage

### For Detection on Images
```bash
./darknet detector test cfg/polyp.data cfg/yolov4-custom.cfg backup/yolov4-custom_best.weights data/test_image.jpg
```

### For Detection on Video
```bash
./darknet detector demo cfg/polyp.data cfg/yolov4-custom.cfg backup/yolov4-custom_best.weights test_video.mp4
```

### For Webcam Detection
```bash
./darknet detector demo cfg/polyp.data cfg/yolov4-custom.cfg backup/yolov4-custom_best.weights
```

## 📁 Project Structure

```
├── cfg/
│   ├── yolov4-custom.cfg      # Custom YOLOv4 configuration for polyp detection
├── backup/                    # Trained model weights
│   ├── yolov4-custom_best.weights
│   └── yolov4-custom_final.weights
├── data/
│    └── Images + Labels.txt   # Data Set Up
│    └── polyp.data
│    └── polyp.names
│    └── train.txt
│    └── test.txt
├── process.py                # To create train.txt and test.txt
├── bad.list                  # List of bad training images
└── README_POLYP_DETECTION.md # This file
```

## 🔧 Configuration

### Model Configuration
- **Input size:** 608x608
- **Classes:** 1 (polyp)
- **Architecture:** YOLOv4
- **Trained iterations:** 6000+

### Dataset Information
- Custom endoscopy dataset
- Single class detection (polyp)
- Augmented training data

## 📊 Performance
- Best weights available in `backup/yolov4-custom_best.weights`
- Training charts available as `chart_yolov4-custom.png`

## 🛠️ Training (Optional)

If you want to retrain the model:

1. Prepare your dataset in YOLO format
2. Update `cfg/polyp.data` with your paths
3. Run training:
```bash
./darknet detector train cfg/polyp.data cfg/yolov4-custom.cfg yolov4.conv.137
```

## 📝 Notes

- The model is specifically trained for endoscopy polyp detection
- GPU acceleration is highly recommended for real-time performance
- Pre-trained weights are included in the backup folder
- For best results, use images similar to the training dataset

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

Copyright (c) 2025 Deepsi

All Rights Reserved.

This repository and its contents are made available solely for **educational and demonstration purposes**.  
The code, documentation, and associated materials herein are intended to showcase the author's technical work and are not licensed for use, reproduction, modification, or distribution in any form.

This project was developed as a **sample representation** of work conducted under a **non-disclosure agreement (NDA)** and therefore **does not include or disclose any proprietary data, models, or intellectual property** belonging to the NDA-bound organization.

By accessing this repository, you agree that:
- You may view and reference the content for **personal, non-commercial learning** only.
- You may **not copy, modify, reproduce, or distribute** any part of this repository.
- You may **not use** this work for research, publication, or commercial applications.

Any unauthorized use, reproduction, or redistribution of this material is strictly prohibited.

For permissions beyond this scope, please contact the author directly.
