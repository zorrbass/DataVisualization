from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice

die_1 = Die()
die_2 = Die()

# Make some rolls and store the results in s list
rolls = 100000
# results = [] /// no more necessary after the use of list comprehension
#"""This block will be changed to a list comprehension"""
#   for roll_num in range(rolls):
#       result = die_1.roll() + die_2.roll()
#       results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(rolls)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides

# frequencies = [] /// no more necessary after the use of list comprehension
#"""This block will be changed to a list comprehension"""
#   for value in range(2, max_result+1):
#       frequency = results.count(value)
#       frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of result"}
my_layout = Layout(title=f"Results of rolling two D6 dice {rolls} times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d6_d6.html")
