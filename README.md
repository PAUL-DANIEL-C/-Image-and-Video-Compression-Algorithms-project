# Image and Video Compression Algorithms

## Overview
This project implements custom image and video compression algorithms using Discrete Cosine Transform (DCT). It includes adjustable quality levels, performance metrics (PSNR, SSIM), and visualization of compressed vs. original media.

## Features
- **Image Compression**: Compress images using DCT-based techniques (similar to JPEG).
- **Video Compression**: Compress video frame-by-frame using DCT.
- **Metrics**: Evaluate compression quality with PSNR and SSIM.
- **Visualization**: Visualize and compare original and compressed media.

## Project Structure
```image-video-compression-algorithms/
├── compress_image.py        # Image compression script
├── compress_video.py        # Video compression script
├── metrics.py               # Script to calculate PSNR, SSIM
├── utils.py                 # Utility functions for compression
├── README.md                # Project description
├── requirements.txt         # Required libraries
├── test_images/             # Test images for compression
└── test_videos/             # Test videos for compression
```

## Getting Started

### Prerequisites
1. Python 3.x
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

### Run Image Compression
```bash
python compress_image.py --input test_images/input.jpg --output test_images/compressed_output.jpg --quality 30
```

### Run Video Compression
```bash
python compress_video.py --input test_videos/input.mp4 --output test_videos/compressed_output.avi --quality 30
```

### Evaluate Compression Quality
```bash
python metrics.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
