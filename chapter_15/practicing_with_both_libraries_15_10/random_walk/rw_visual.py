from plotly.graph_objs import Scatter
from plotly import offline
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()

trace = Scatter(x=rw.x_values, y=rw.y_values, 
        mode='markers', marker=dict(size=10))
start = Scatter(x=[0], y=[0],
        mode='markers', marker=dict(size=10, color='green'))
end = Scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]],
        mode='markers', marker=dict(size=10, color='red'))

offline.plot([trace, start, end], filename='random_walk.html')