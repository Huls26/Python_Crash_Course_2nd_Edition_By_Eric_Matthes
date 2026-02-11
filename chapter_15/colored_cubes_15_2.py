import matplotlib.pyplot as plt

# First 5 cubes
raise_5_x_values = range(1, 6)
raise_5_y_values = [x**3 for x in raise_5_x_values]

# First 5000 cubes
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

# Highlight first 5 cubes
ax.scatter(raise_5_x_values, raise_5_y_values, c=raise_5_y_values, cmap=plt.cm.Blues, s=1)

# Colored plot for 5000 cubes
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.inferno, s=1)

# Titles and labels
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.show()
