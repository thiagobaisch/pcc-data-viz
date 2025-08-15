import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #Creates a randomwalk
    rw = RandomWalk(10000)
    rw.fill_walk()

    #Exibits the data as a plot
    plt.style.use('ggplot')
    fig, ax = plt.subplots()

    #Added comment
    #We add here a colormap to see the progression of the randomwalk
    #point_numbers is to get the list of points to apply the colormap
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    #Plotting the first and end points different
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    #Personalizations
    #Removing axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    #Set spacing from each label from both axis to be equal
    ax.set_aspect('equal')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break