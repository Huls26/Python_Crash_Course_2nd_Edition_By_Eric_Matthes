import matplotlib.pyplot as plt

from die import Die

# Create a D6.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(1_000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

plt.style.use('_mpl-gallery')

# Visualize the results.
x_values = list(range(2, max_result+1))

# x_axis_config = {'title': 'Result', 'dtick': 1}
# y_axis_config = {'title': 'Frequency of Result'}
# my_layout = Layout(title='Results of rolling two D6 dice 1,000 times',
#  xaxis=x_axis_config, yaxis=y_axis_config)

# plot
fig, ax = plt.subplots()

ax.bar(x_values, frequencies, width=1, edgecolor="white", linewidth=5)

# Set chart title and label axes.
ax.set_title("Results of rolling two D6 dice 1,000 times", fontsize=24)
ax.set_xlabel("result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
