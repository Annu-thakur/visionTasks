import cv2
import matplotlib.pyplot as plt

# Read the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Perform histogram equalization
equalized = cv2.equalizeHist(image)

# Save the equalized image
cv2.imwrite("output.png", equalized)

# Create before and after histogram comparison
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.hist(image.ravel(), 256, [0, 256])
plt.title("Before Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.subplot(1, 2, 2)
plt.hist(equalized.ravel(), 256, [0, 256])
plt.title("After Equalization")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

plt.tight_layout()

# Save histogram comparison
plt.savefig("histogram_comparison.png", bbox_inches="tight")
plt.close()

print("Equalized image saved as output.png")
print("Histogram comparison saved as histogram_comparison.png")