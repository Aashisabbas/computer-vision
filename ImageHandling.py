from PIL import Image

# Open an image file
image = Image.open('C:/Users/surya/PycharmProjects/pythonProject/thalapathy.jpg')

# Show the image
image.show()

# Get the size of the image
width, height = image.size
print("Image size:", width, "x", height)

# Convert the image to grayscale
gray_image = image.convert('L')
gray_image.show()

# Resize the image
resized_image = image.resize((width // 2, height // 2))
resized_image.show()

# Rotate the imageC:/Users/surya/PycharmProjects/pythonProject/thalapathy.jpg
rotated_image = image.rotate(90)
rotated_image.show()

# Save the modified image
rotated_image.save('rotated_example.jpg')