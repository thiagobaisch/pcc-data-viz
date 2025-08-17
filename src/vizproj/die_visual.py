from die import Die
import plotly.express as px

die = Die()

#Create some tests and stores it in list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


#Analyses results
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Creating the display
#Personalizations
title = 'Results of rolling one D6 1000 times'
labels = {'x': 'Result' , 'y':'Frequency of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
#I need to use renderer='browser' because the default is a jupyter notebook, and this is not inside one
fig.show(renderer='browser')
