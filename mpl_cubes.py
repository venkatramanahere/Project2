import matplotlib.pyplot as plt

input_values = range(1, 5001)
cubes = [x**3 for x in input_values]

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.plot(input_values, cubes, linewidth = 3)

# Set chart title and label axes.
ax.set_title("Cubes of Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Cube of Value", fontsize = 14)

# Set size of tick labels.
ax.tick_params(labelsize = 14)

plt.show()
