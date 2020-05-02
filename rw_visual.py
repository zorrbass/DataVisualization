import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new random walks
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors="none", s=2)
    # ax.axis([-400, 400, -400, 400])

    # Emphasize the first and the last point
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none",
               s=100)

    # Remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_drawing = input("Do you want to continue y/n ?")
    if keep_drawing == "n":
        break

