import cv2

# Read the color image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: input.jpg not found")
    exit()

# Convert color image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get image information
height, width = gray.shape

print("Original Image Shape:", image.shape)
print("Grayscale Image Shape:", gray.shape)
print("Height:", height)
print("Width:", width)

# Save the grayscale image
cv2.imwrite("output.png", gray)

print("Grayscale image saved as output.png")