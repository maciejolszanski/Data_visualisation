from plotly.graph_objects import Scatter, Layout
from plotly import offline 
from random_walk import Randomwalk


rw = Randomwalk(100_000)
rw.fill_walk()
point_number = range(rw.num_points)
data = Scatter(x=rw.x_values, y=rw.y_values, mode="markers")
# data2 = Scatter(x=0, y=0, mode='markers')

x_axis_conf = {'title': 'x'}
y_axis_conf = {'title': 'y'}
my_lay = Layout(title="Błądzenie losowe", xaxis=x_axis_conf, yaxis=y_axis_conf)

offline.plot({'data': data, 'layout': my_lay}, filename= 'rw_plotly.html')