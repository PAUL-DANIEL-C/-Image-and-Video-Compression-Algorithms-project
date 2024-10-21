import cv2
import numpy as np

def dct2(block):
    """Apply 2D Discrete Cosine Transform to an 8x8 block."""
    return cv2.dct(np.float32(block))

def idct2(block):
    """Apply inverse 2D Discrete Cosine Transform."""
    return cv2.idct(np.float32(block))

def compress_image(image_path, output_path, quality=50):
    """Compress the image using DCT."""
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    h, w = img.shape

    # Create a new image for the compressed output
    compressed_img = np.zeros_like(img)

    block_size = 8  # DCT operates on 8x8 blocks
    for i in range(0, h, block_size):
        for j in range(0, w, block_size):
            block = img[i:i+block_size, j+j+block_size]
            dct_block = dct2(block)
            # Keep only the top 'quality' DCT coefficients
            dct_block[quality:] = 0
            compressed_img[i:i+block_size, j+j+block_size] = idct2(dct_block)
    
    # Save the compressed image
    cv2.imwrite(output_path, compressed_img)
    print(f"Compressed image saved as {output_path}")

if __name__ == "__main__":
    # Example usage
    compress_image('test_images/sample1.jpg', 'test_images/compressed_output.jpg', quality=30)

