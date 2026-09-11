import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Custom sharpening kernel
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

# Apply the sharpening kernel
sharpened = cv2.filter2D(image, -1, kernel)

# Save the sharpened image
cv2.imwrite("output.png", sharpened)

print("Sharpened image saved as output.png")