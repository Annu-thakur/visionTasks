import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply smoothing using Gaussian Blur
smooth = cv2.GaussianBlur(image, (5, 5), 0)

# Create a sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply sharpening
sharp = cv2.filter2D(image, -1, kernel)

# Save both results
cv2.imwrite("output_smooth.png", smooth)
cv2.imwrite("output_sharp.png", sharp)

print("Smoothed image saved as output_smooth.png")
print("Sharpened image saved as output_sharp.png")