from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_vtk
import vtk
from dash_vtk.utils import to_mesh_state

# Load the OBJ file
reader = vtk.vtkOBJReader()
reader.SetFileName("./assets/brain2.obj")
reader.Update()
polydata = reader.GetOutput()
mesh_state = to_mesh_state(polydata)


# import pdb; pdb.set_trace()


def create_layout():
    """Build layout"""
    return dbc.Container([dbc.Row([plot_pane()])], fluid=True)


def plot_pane():
    """Plot pane"""
    return html.Div(
        dash_vtk.View(
            id="vtk-view",
            triggerRender=1.0,
            children=[
                dash_vtk.GeometryRepresentation(
                    showCubeAxes=True,
                    # cubeAxesStyle={
                    #     "height": 2000,
                    #     "startingHeight": 10,
                    #     "width": 2000,
                    #     },
                    property={
                        "edgeVisibility": False,
                        # "VertexVisibility": True,
                        "EdgeColor": [0.0, 0.0, 0.0],
                        "VertexColor": [1.0, 1.0, 1.0],
                        "Color": [0.2, 0.6, 0.7],
                        "Opacity": 0.5,
                    },
                    children=[dash_vtk.Mesh(state=mesh_state)],
                )
            ],
            style={"height": "100vh", "width": "100vw"}
        ),
        style={"height": "100%", "width": "100%"}
    )
