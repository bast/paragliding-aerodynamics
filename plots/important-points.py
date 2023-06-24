# SPDX-FileCopyrightText: 2023 Radovan Bast <radovan.bast@uit.no>
#
# SPDX-License-Identifier: MIT

from data import data
from colors import colors

import plotly.graph_objects as go

xs, ys = zip(*data["2023 beginner wing"])

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=xs,
        y=ys,
        mode="lines",
        line_shape="spline",
        name="polar",
    )
)

fig.update_traces(
    selector=dict(name="polar"),
    line=dict(width=4, color=colors["reddishpurple"]),
)

fig.update_xaxes(
    title_text="Horizontal speed (m/s)",
    range=[0, 15],
    title_standoff=0,
    ticks="outside",
    tickcolor="lightgray",
    ticklen=10,
    side="top",
)

fig.update_yaxes(
    title_text="Vertical speed (m/s)",
    range=[-1.75, 0],
    title_standoff=0,
    ticks="outside",
    tickcolor="lightgray",
    ticklen=10,
    tickformat=".1f",
)

points = {
    "min speed": (7.65, -1.2),
    "min sink": (9.15, -0.9),
    "best glide": (11.1, -1.0),
    "max speed": (14.45, -1.5),
}

for name, (x, y) in points.items():
    fig.add_trace(
        go.Scatter(
            x=[0.0, x],
            y=[0.0, y],
            mode="lines",
            name=name,
        )
    )

    fig.update_traces(selector=dict(name=name), line=dict(dash="dash", color="black"))

    fig.add_annotation(
        x=x,
        y=y,
        text=name,
        showarrow=True,
        arrowcolor=colors["blue"],
        arrowhead=2,
        arrowsize=1.5,
        ax=0,
        ay=40,
    )

fig.update_layout(showlegend=False)

fig.write_image("important-points.svg")
