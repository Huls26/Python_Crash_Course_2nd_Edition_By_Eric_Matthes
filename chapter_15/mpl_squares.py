# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

print(plt.style.available)
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()