from dash import Input, Output, no_update, Patch
from colors import vertexcolor_1, vertexcolor_2


def create_callbacks(app):
    """Create sidebar callbacks"""

    @app.callback(
        Output("brain_graph", "figure"),
        Input("trigger", "n_intervals"),
        prevent_initial_call=True,
    )
    def _change_color(n_intervals):
        if not n_intervals:
            return no_update

        patched_figure = Patch()

        colors = vertexcolor_1 if n_intervals % 2 else vertexcolor_2

        patched_figure["data"][0]["vertexcolor"] = colors

        return patched_figure
