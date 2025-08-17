from die import Die
import plotly.express as px

die_1 = Die(6)
die_2 = Die(6)

#Create some tests and stores it in list
number_of_rolls = 10000
results = [die_1.roll() + die_2.roll() for _ in range(number_of_rolls)]

#Analyses results
max_result = die_1.num_sides + die_2.num_sides 
poss_results = range(1, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

#Creating the display
#Personalizations
title = 'Results of rolling two D6 1000 times'
labels = {'x': 'Result' , 'y':'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
#I need to use renderer='browser' because the default is a jupyter notebook, and this is not inside one
fig.show(renderer='browser')
