import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Choose brightness value
brightness = 50

# Store one pixel value before enhancement
before = image[100, 100].copy()

# Increase brightness and keep pixel values within 0-255
bright_image = cv2.add(image, np.full(image.shape, brightness, dtype=np.uint8))

# Store the same pixel value after enhancement
after = bright_image[100, 100].copy()

# Print before and after pixel values
print("Pixel value before enhancement:", before)
print("Pixel value after enhancement:", after)

# Save the enhanced image
cv2.imwrite("output.png", bright_image)

print("Brightness enhanced image saved as output.png")