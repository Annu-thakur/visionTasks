import cv2

# Read the image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Apply mean filter with 3x3 kernel
mean_3x3 = cv2.blur(image, (3, 3))

# Apply mean filter with larger 5x5 kernel
mean_5x5 = cv2.blur(image, (5, 5))

# Save the final output using the larger kernel
cv2.imwrite("output.png", mean_5x5)

print("3x3 mean filter applied.")
print("5x5 mean filter applied.")
print("Final output saved as output.png")