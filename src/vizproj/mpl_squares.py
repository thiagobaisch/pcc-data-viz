# Basic ploting of a line graph. 

import matplotlib.pyplot as plt

#Setting style for the graphs
plt.style.use('ggplot')

#Data used
input_values =[1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#fig is a figure - which is the collection of graphs generated
#ax represents a single graph in the figure
fig, ax = plt.subplots()

#This plots the graph using the data on ax
ax.plot(input_values, squares, linewidth=3)

#This commands are for personalizing the graph, setting labels and changing fontsize
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Change the fontsize of the axes labels
ax.tick_params(labelsize=14)

#Creates the graph
plt.show()

 