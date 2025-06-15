import matplotlib.pyplot as plt

numbers = range(6)
squares = [n**2 for n in range(6)]

plt.style.use('Solarize_Light2') 
fig, ax = plt.subplots() # fig for the entire figure, ax for individual plot
ax.plot(numbers, squares, linewidth=3)

# Chart title and label axes.
ax.set_title("Square Numbers", fontsize=18)
ax.set_xlabel("Value", fontsize=12)
ax.set_ylabel("Square of Value", fontsize=12)

# Size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
