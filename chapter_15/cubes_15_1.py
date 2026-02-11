import matplotlib.pyplot as plt

raise_5_x_values = range(1, 6)
raise_5_y_values = [x**3 for x in raise_5_x_values]
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

ax.scatter(raise_5_x_values, raise_5_y_values, s=10)
ax.plot(x_values, y_values, linewidth=1)

# Set chart title and label axes.
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)

plt.show()