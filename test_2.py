import plotly.graph_objects as go

fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[1, 3, 2])],
    layout_title_text="A Figure Specified By A Graph Object"
)

fig.write_html('species.html', auto_open=True)
# fig.show()