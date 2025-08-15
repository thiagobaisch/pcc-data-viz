import matplotlib.pyplot as plt

plt.style.use('ggplot')

#Generate data
x_values = range(1,5001)
y_values = [x**3 for x in x_values]

#Create graph
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=5)

#Personalize
ax.set_title('Cubic Numbers')
ax.set_xlabel('Values')
ax.set_ylabel('Cubic of Value')

#Plot
plt.show()

