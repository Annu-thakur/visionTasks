import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: input.jpg not found")
    exit()

# Convert image to float32
image_float = np.float32(image)

# Compute the 2D DFT
dft = cv2.dft(image_float, flags=cv2.DFT_COMPLEX_OUTPUT)

# Shift low frequencies to the center
dft_shift = np.fft.fftshift(dft)

# Get image dimensions
rows, cols = image.shape
crow, ccol = rows // 2, cols // 2

# Create a high-pass mask
mask = np.ones((rows, cols, 2), np.float32)

# Suppress the central low-frequency region
radius = 30

for y in range(rows):
    for x in range(cols):
        distance = np.sqrt((y - crow) ** 2 + (x - ccol) ** 2)

        if distance <= radius:
            mask[y, x] = 0

# Apply the high-pass mask
filtered_dft = dft_shift * mask

# Shift frequencies back
dft_ishift = np.fft.ifftshift(filtered_dft)

# Perform inverse DFT
result = cv2.idft(dft_ishift)

# Calculate magnitude
result = cv2.magnitude(result[:, :, 0], result[:, :, 1])

# Normalize result to 0-255
result = cv2.normalize(result,None,0,255,cv2.NORM_MINMAX)

# CONVERT RESULT TO uint8
result = np.uint8(result)

# save the output image
cv2.imwrite("output.png",result)

# display the result 
cv2.imshow("High Pass Filtered Image",result)

# wait for a key press
cv2.waitKey(0)

# close all windows
cv2.destroyALLWindows()