import cv2

# Read the noisy image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Use a 5x5 odd kernel for effective Gaussian smoothing
kernel_size = (5, 5)

# Apply Gaussian smoothing
gaussian_image = cv2.GaussianBlur(image, kernel_size, 0)

# Save the smoothed image
cv2.imwrite("output.png", gaussian_image)

print("Gaussian smoothing applied successfully.")
print("Output saved as output.png")