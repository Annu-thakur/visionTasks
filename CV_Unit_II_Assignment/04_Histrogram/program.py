import cv2
import matplotlib.pyplot as plt

# Read image in grayscale
image = cv2.imread("input.jpg", 0)

# Calculate histogram
histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

# Find intensity with highest frequency
highest = histogram.argmax()

print("Intensity value with highest frequency:", highest)

# Display histogram
plt.plot(histogram)
plt.title("Image Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")

# Save histogram
plt.savefig("output.png")
plt.close()

print("Histogram saved as output.png")