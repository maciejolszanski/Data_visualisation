from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# create dies (default it is D6)
die1 = Die()
die2 = Die()

rolls = 500_000

# roll the die few times and write the results to list
results = [die1.roll() * die2.roll() for roll_num in range(rolls)]

# analise the results
max_result = die1.num_sides * die2.num_sides 
frequencies = [results.count(value) for value in range(2, max_result+1)]

# visualising the results
x_val = list(range(2, max_result))
data = [Bar(x=x_val, y=frequencies)]

x_axis_conf = {'title': 'Wynik', 'dtick': 1}
y_axis_conf = {'title': 'Częstotliwość występowania wartości'}

my_layout = Layout(
    title=f"Wynik rzucania kośćmi D6 i D6 {rolls} razy",
    xaxis=x_axis_conf,
    yaxis=y_axis_conf,
    )

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')
