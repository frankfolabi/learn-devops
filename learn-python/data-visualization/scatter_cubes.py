import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots() # fig for the entire figure, ax for individual plot
ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

# Chart title and label axes.
ax.set_title("Cube Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Cube of Value", fontsize=12)

# Size of tick labels.
ax.tick_params(labelsize=14)

# Range for each axis.
ax.axis([0, 5100, 0, 125_100_000_000])

plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()