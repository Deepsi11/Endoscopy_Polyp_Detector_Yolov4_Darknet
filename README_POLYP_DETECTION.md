# Endoscopy Polyp Detector using YOLOv4 Darknet

This repository contains a complete YOLOv4 implementation for detecting polyps in endoscopy images using the Darknet framework.

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
│   └── polyp.data             # Dataset configuration
├── backup/                    # Trained model weights
│   ├── yolov4-custom_best.weights
│   └── yolov4-custom_final.weights
├── data/
│   └── polyp.names           # Class names file
├── process.py                # Data processing utilities
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

This project uses the Darknet framework. Please refer to the original Darknet license.