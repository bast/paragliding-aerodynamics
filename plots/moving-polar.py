# SPDX-FileCopyrightText: 2023 Radovan Bast <radovan.bast@uit.no>
#
# SPDX-License-Identifier: MIT

from data import data
from colors import colors

import plotly.graph_objects as go

xs, ys = zip(*data["2023 beginner wing"])

displacements_and_glides = [
    ((5.0, 0.0), (16.3, -1.0), "polar-tailwind"),
    ((-7.0, 0.0), (7.5, -1.5), "polar-headwind"),
    ((0.0, 0.5), (9.5, -0.4), "polar-lift"),
    ((0.0, -2.0), (14.5, -3.5), "polar-sink"),
    ((11.1 / 4, -1.0 / 4), (11.1 * 1.25, -1.0 * 1.25), "polar-adding-weight"),
]

for (dx, dy), (gx, gy), name in displacements_and_glides:
    fig = go.Figure()

    fig.update_layout(showlegend=False, width=800, height=800)

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
        range=[-3.5, 0],
        title_standoff=0,
        ticks="outside",
        tickcolor="lightgray",
        ticklen=10,
        tickformat=".1f",
    )

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
        opacity=0.4,
    )

    fig.add_trace(
        go.Scatter(
            x=[x + dx for x in xs],
            y=[y + dy for y in ys],
            mode="lines",
            line_shape="spline",
            name="polar",
        )
    )

    fig.update_traces(
        selector=dict(name="polar"),
        line=dict(width=4, color=colors["reddishpurple"]),
    )

    fig.add_trace(
        go.Scatter(
            x=[0.0, gx],
            y=[0.0, gy],
            mode="lines",
            name="best glide",
        )
    )

    fig.update_traces(
        selector=dict(name="best glide"), line=dict(dash="dash", color="black")
    )

    fig.write_image(f"{name}.svg")
