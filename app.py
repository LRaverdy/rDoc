import plotly.express as px
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, callback, State

app = dash.Dash(
    __name__,
    use_pages=True,
    pages_folder="pages",
    external_stylesheets=[dbc.themes.DARKLY],
    suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport','content': 'width=device-width, initial-scale=1 , maximum-scale=1.9, minimum-scale=.5'}])
'''auth = dash_auth.BasicAuth(
    app,
    cred
)'''


server = app.server

menu = dbc.DropdownMenu([
    dbc.DropdownMenuItem("Home", href="/"),
    dbc.DropdownMenuItem("Plotly", href="plotly"),
    dbc.DropdownMenuItem("Pandas", href="pandas"),
],
    nav=True,
    label="Menu"
)

app.layout = html.Div([
    dbc.Navbar(
        dbc.Container([
            dbc.Col([
            dbc.NavbarBrand(
                "rDoc",
                href="",
                #className="bar-brand logo my-navbar"
            )
            ], xl=3),

            dbc.NavbarToggler(id="navbar-toggler1"),

            dbc.Collapse(

                dbc.Nav(
                    menu,
                    className="ms-auto my-navbar",
                    navbar=True
                ),
                id="navbar-collapse1",
                navbar=True,
            ),
        ], className="my-navbar"),
        className="my-navbar",
        dark=True,
        #fixed="top",
        sticky="top"
    ),

                # content of each page
                html.Div([dash.page_container]
                         #style={"paddingTop": 160}
                         )

    ])

# we use a callback to toggle the collapse on small screens
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# the same function (toggle_navbar_collapse) is used in all three callbacks
for i in [1]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


if __name__ == "__main__":
    app.run_server(host='localhost', port=3000, debug=True)