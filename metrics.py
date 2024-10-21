import cv2
import numpy as np
import math

def calculate_psnr(original, compressed):
    """Calculate the PSNR between original and compressed images."""
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:  # No noise is present in the signal.
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * math.log10(max_pixel / math.sqrt(mse))
    return psnr

def calculate_ssim(original, compressed):
    """Calculate SSIM between original and compressed images."""
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    mu1 = cv2.GaussianBlur(original, (11, 11), 1.5)
    mu2 = cv2.GaussianBlur(compressed, (11, 11), 1.5)
    sigma1_sq = cv2.GaussianBlur(original ** 2, (11, 11), 1.5) - mu1 ** 2
    sigma2_sq = cv2.GaussianBlur(compressed ** 2, (11, 11), 1.5) - mu2 ** 2
    sigma12 = cv2.GaussianBlur(original * compressed, (11, 11), 1.5) - mu1 * mu2

    ssim_map = ((2 * mu1 * mu2 + c1) * (2 * sigma12 + c2)) / ((mu1 ** 2 + mu2 ** 2 + c1) * (sigma1_sq + sigma2_sq + c2))
    return ssim_map.mean()

if __name__ == "__main__":
    # Load original and compressed images for testing
    original = cv2.imread('test_images/input.jpg', cv2.IMREAD_GRAYSCALE)
    compressed = cv2.imread('test_images/compressed_output.jpg', cv2.IMREAD_GRAYSCALE)

    psnr_value = calculate_psnr(original, compressed)
    ssim_value = calculate_ssim(original, compressed)

    print(f"PSNR: {psnr_value}")
    print(f"SSIM: {ssim_value}")
