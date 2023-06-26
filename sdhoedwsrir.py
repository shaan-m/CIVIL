import matplotlib.pyplot as plt

# Load the image
image = plt.imread("c:/Users/LYZEN/Downloads/Hel.jpg")

# Display the image
plt.imshow(image)
plt.axis('off')

# Use the ginput function to interactively select a point
point = plt.ginput(1, timeout=-1)

# Close the figure
plt.close()

# Extract the x and y coordinates of the selected point
x_coord = point[0][0]
y_coord = point[0][1]

# Print the coordinates
print("Selected Coordinate:")
print("x:", x_coord)
print("y:", y_coord)
