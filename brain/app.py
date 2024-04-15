import dash
import dash_bootstrap_components as dbc
from layout.layout import create_layout

EXTERNAL_STYLESHEETS = [dbc.themes.MINTY]

APP = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)
APP.layout = create_layout


# def create_callbacks(app):
#     """Create all callbacks"""
#     src.callbacks.card.create_callbacks(app)
#     src.callbacks.deck.create_callbacks(app)
#     src.callbacks.config.create_callbacks(app)
#     src.callbacks.plot.create_callbacks(app)
#     src.callbacks.serializer.create_callbacks(app)
#     src.callbacks.config_import.create_callbacks(app)
#     src.callbacks.deserializer.create_callbacks(app)


# create_callbacks(APP)


# Run the Dash app
if __name__ == "__main__":
    APP.run_server(debug=True)
