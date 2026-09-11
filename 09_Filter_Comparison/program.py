import cv2

# Read the noisy image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply Mean filter
mean = cv2.blur(image, (5, 5))

# Apply Gaussian filter
gaussian = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Median filter
median = cv2.medianBlur(image, 5)

# Save all three results
cv2.imwrite("output_mean.png", mean)
cv2.imwrite("output_gaussian.png", gaussian)
cv2.imwrite("output_median.png", median)

print("Mean filter output saved as output_mean.png")
print("Gaussian filter output saved as output_gaussian.png")
print("Median filter output saved as output_median.png")