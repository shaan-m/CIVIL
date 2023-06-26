import matplotlib.pyplot as plt

x = [0, 1, 1, 0, 0]
y1 = [0, 0, 2, 2, 0]
y2 = [0, 0, 1, 1, 0]

fig, ax = plt.subplots()

# Plot the first line
ax.plot(x, y1, label='Line 1',color='black')

# Plot the second line
ax.plot(x, y2, label='Line 2',color='red')

# Add a legend

plt.show()
