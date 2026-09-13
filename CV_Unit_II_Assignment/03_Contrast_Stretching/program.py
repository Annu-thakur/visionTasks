import cv2
import numpy as np

# Read the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Find minimum and maximum intensity values
min_value = np.min(image)
max_value = np.max(image)

print("Minimum intensity:", min_value)
print("Maximum intensity:", max_value)

# Perform contrast stretching
if max_value != min_value:
    stretched = ((image - min_value) * 255.0 /
                 (max_value - min_value))

    # Convert to 8-bit image
    stretched = np.uint8(stretched)
else:
    stretched = image.copy()

# Save the enhanced image
cv2.imwrite("output.png", stretched)

print("Contrast stretched image saved as output.png")