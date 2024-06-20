import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    # point_numbers = range(rw.num_points)
    # cmap = plt.cm.Blues
    ax.plot(rw.x_values, rw.y_values, linewidth=0.5)
    ax.set_aspect('equal')

    # Emphasize the first and last points.
    # ax.plot(0, 0, linewidth=25, color = 'green')
    # ax.plot(rw.x_values[-1], rw.y_values[-1], linewidth=25, color = 'red')

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
