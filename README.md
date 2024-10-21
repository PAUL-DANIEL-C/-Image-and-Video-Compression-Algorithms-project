# Image and Video Compression Algorithms

## Overview
This project implements both image and video compression algorithms using common techniques like Discrete Cosine Transform (DCT) and wavelet transforms. The goal is to explore the trade-offs between file size reduction and the quality loss inherent to compression techniques.

## Features
- **Image Compression**: Implements DCT-based image compression (similar to JPEG).
- **Video Compression**: Basic video compression using frame-by-frame image compression.
- **Adjustable Quality Levels**: Control over compression level to prioritize either quality or file size.
- **Performance Metrics**: Calculate PSNR (Peak Signal-to-Noise Ratio) and SSIM (Structural Similarity Index) to evaluate compression quality.
- **Visualization**: Compare original and compressed images/videos and display quality metrics graphically.

## Compression Techniques
- **DCT (Discrete Cosine Transform)**: Basis of JPEG compression.
- **Wavelet Transform**: Used for advanced image compression.
- **Run-Length Encoding**: Optional method to further compress image data by simplifying repeating pixel values.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-video-compression-algorithms.git
