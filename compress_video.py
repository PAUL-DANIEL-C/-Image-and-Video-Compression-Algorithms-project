import cv2
from compress_image import compress_image

def compress_video(input_video_path, output_video_path, quality=50):
    """Compress video by applying DCT compression to each frame."""
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor=False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        compressed_frame = np.zeros_like(gray_frame)

        block_size = 8
        for i in range(0, height, block_size):
            for j in range(0, width, block_size):
                block = gray_frame[i:i+block_size, j+j+block_size]
                dct_block = dct2(block)
                dct_block[quality:] = 0
                compressed_frame[i+i+block_size, j+j+block_size] = idct2(dct_block)
        
        # Write the compressed frame to the output video
        out.write(compressed_frame)

    cap.release()
    out.release()
    print(f"Compressed video saved as {output_video_path}")

if __name__ == "__main__":
    compress_video('test_videos/input.mp4', 'test_videos/compressed_output.avi', quality=30)
