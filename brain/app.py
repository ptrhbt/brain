import dash
import dash_bootstrap_components as dbc
from layout.layout import create_layout
from callbacks.graph import create_callbacks

EXTERNAL_STYLESHEETS = [dbc.themes.MINTY]

APP = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
APP.layout = create_layout


create_callbacks(APP)


# Run the Dash app
if __name__ == "__main__":
    APP.run_server(debug=True)
