from plotly.graph_objs import Scatter, Layout, Figure
from plotly import offline
from random_walk import RandomWalk

# Make a random walk.
rw = RandomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))

trace = Scatter(x=rw.x_values, y=rw.y_values, 
        mode='markers', marker=dict(
            size=10,
            color=point_numbers,
            colorscale='Blues',
            showscale=True            
                                    ))
start = Scatter(x=[0], y=[0],
        mode='markers', marker=dict(size=10, color='green'))
end = Scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]],
        mode='markers', marker=dict(size=10, color='red'))

layout = Layout(title='Random Walk', xaxis=dict(title='X'), yaxis=dict(title='Y'))
fig = Figure(data=[trace, start, end], layout=layout)
offline.plot(fig, filename='random_walk.html')