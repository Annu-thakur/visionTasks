import cv2

# Read the noisy image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply median filter to reduce salt-and-pepper noise
filtered_image = cv2.medianBlur(image, 5)

# Save the filtered image
cv2.imwrite("output.png", filtered_image)

print("Median filtered image saved as output.png")