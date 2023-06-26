import matplotlib.pyplot as plt
from tabulate import tabulate
# Create a figure and axis
fig, ax = plt.subplots()
fig, axd = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')
w=input("Enter width of plot (in feet) : ")
l=input("Enter length of the plot (in feet) : ")
# Define the coordinates of the square
x = [0, w, w, 0, 0]
y = [0, 0, l, l, 0]

a = int(input("Enter number of rooms required for the floor : "))

room_name = []       # Initialize an empty list for room names
room_width = []      # Initialize an empty list for room widths
room_length = []     # Initialize an empty list for room lengths
civ_width = []       # Initialize an empty list for civil width coordinates
civ_length = []      # Initialize an empty list for civil length coordinates

for i in range(a):
    room_name.append(input("Enter the type of room: "))
    room_width.append(input("Enter the width of room: "))
    room_length.append(input("Enter the length of room: "))
    print(room_name)
    print(room_width)
    print(room_length)
    civ_width.append([0, room_width[i], room_width[i], 0, 0])
    civ_length.append([0, 0, room_length[i], room_length[i], 0])

# Set the limits of the axes
axd['right'].set_xlim(0, float(w))
axd['right'].set_ylim(0, float(l))
axd['upleft'].axis('off')
ax.set_xticks([])
ax.set_yticks([])
plt.show()
''' 
for i in range(a):
    ax.plot(civ_width,civ_length,color='red')
 
    table = tabulate(room_name, tablefmt="fancy_grid")

print(table)

# Show the plot
ax.set_xlim(0, w)
ax.set_ylim(0, l)
w = [0, 1, 1, 0, 0]
z = [0, 0, 1, 1, 0]
# Set the aspect ratio to equal to make the square appear as a square
ax.set_aspect('equal')
# Set labels and title

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Square')
'''