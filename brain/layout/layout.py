import numpy as np
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from colors import x, y, z, i, j, k, face_colors_1

fig = go.Figure(
    data=[
        go.Mesh3d(
            x=x,
            y=y,
            z=z,
            i=i,
            j=j,
            k=k,
            opacity=0.9,
            name="",
            showscale=False,
            hoverinfo="none",
            facecolor=face_colors_1,
        )
    ],
    layout=go.Layout(autosize=True, height=800),
)


def create_layout():
    """Build layout"""
    return dbc.Container(
        [
            dbc.Row(
                [
                    plot_pane(),
                    dcc.Interval(
                        id="trigger",
                        interval= 0.2 * 1000,  # in milliseconds
                        n_intervals=0,
                    ),
                ]
            )
        ],
        fluid=True,
    )


def plot_pane():
    """Plot pane"""
    return html.Div(
        dcc.Graph(
            id="brain_graph",
            figure=fig,
        ),
        style={"height": "100vh", "width": "100vw"},
    )
