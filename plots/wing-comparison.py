from data import data
from colors import colors
from interpolation import fit

import plotly.graph_objects as go


fig = go.Figure()

color_iterator = iter(colors.items())

for name, points in data.items():
    xs, ys = zip(*points)
    xs_fit, ys_fit = fit(xs, ys)
    fig.add_trace(
        go.Scatter(
            x=xs_fit,
            y=ys_fit,
            mode="lines",
            name=name,
        )
    )
    fig.update_traces(
        selector=dict(name=name), line=dict(width=4, color=next(color_iterator)[1])
    )

fig.update_xaxes(
    title_text="Horizontal speed (m/s)",
    range=[0, 20],
    title_standoff=0,
    ticks="outside",
    tickcolor="lightgray",
    ticklen=10,
    side="top",
)

fig.update_yaxes(
    title_text="Vertical speed (m/s)",
    range=[-2.5, 0],
    title_standoff=0,
    ticks="outside",
    tickcolor="lightgray",
    ticklen=10,
    tickformat=".1f",
)

fig.write_image("wing-comparison.svg")
