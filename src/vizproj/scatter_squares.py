import matplotlib.pyplot as plt
plt.style.use("ggplot")

#Data
x_values = range(1,1001)
y_values = [x**2 for x in x_values]


fig,ax = plt.subplots()
#Colormap - sequence of colors in a gradient, that goes from an inicial color to another. pyplot have many builtin
#colormaps, which are applied here using c=y_values (assign a sequence of values to a colormap) 
# and cmap=plt.cm.Blues (applies colormap)
ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)

#Size of scale parameters on the axis
ax.tick_params(labelsize=14)
#Set to use plain values instead of cientific notation
ax.ticklabel_format(style='plain')

#Set each axis interval
ax.axis([0, 1100, 0, 1_100_000])

#Saves a figure of the graph instead of showing it
#plt.savefig('square_plot.png', bbox_inches='tight')
plt.show()