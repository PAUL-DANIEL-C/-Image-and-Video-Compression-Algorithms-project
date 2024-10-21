import cv2
import numpy as np

def dct2(block):
    """Apply 2D Discrete Cosine Transform to an 8x8 block."""
    return cv2.dct(np.float32(block))

def idct2(block):
    """Apply inverse 2D Discrete Cosine Transform."""
    return cv2.idct(np.float32(block))

def split_into_blocks(image, block_size=8):
    """Split the image into blocks of size block_size x block_size."""
    h, w = image.shape
    return [image[i:i+block_size, j:j+block_size] for i in range(0, h, block_size) for j in range(0, w, block_size)]

def merge_blocks(blocks, image_shape, block_size=8):
    """Merge blocks back into an image."""
    h, w = image_shape
    img = np.zeros(image_shape, dtype=np.float32)
    index = 0
    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            img[i:i+block_size, j:j+block_size] = blocks[index]
            index += 1
    return img
