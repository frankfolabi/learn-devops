import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots() # fig for the entire figure, ax for individual plot
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Chart title and label axes.
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

# Size of tick labels.
ax.tick_params(labelsize=14)

# Range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

plt.savefig('squares_plot.png', bbox_inches='tight')
