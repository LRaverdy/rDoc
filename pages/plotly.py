import dash
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output, callback, dash_table
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import graphs as g


dash.register_page(__name__, path='/plotly')

layout = dbc.Container([
    html.H2("Potly Express"),

    dbc.Row([
        html.H3("Bar")
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
            dcc.Graph(figure=g.fifa(), className="graph"),

            dcc.Markdown('''
            ```python
            
            fig = px.bar(
                    scores,
                    x='percentage',
                    y='game',
                    color='score',
                    text='percentage',
                    color_continuous_scale=['red', 'yellow', 'lightgreen'],
                    hover_data=scores
            )
    
            fig.update_layout(
                height=300,
                width=700,
                title="<b>Score : PES vs FIFA</b>",
                title_x = 0.5,
                xaxis_title='Percentage',
                yaxis_title=None,
            )
            
            fig.update_traces(
                texttemplate='<b>%{text} %</b>',
                textposition='inside', 
                textfont_size=12,
                insidetextanchor="middle"
            )
            
            fig.show()
            
            ```''',
                className="invert"
        )
            ], className="card")
        ]),

        dbc.Card([
            dcc.Graph(figure=g.sales_mrr(), className="graph"),
            dcc.Markdown(g.sales_mrr_code)
    ], className="card"),


        dbc.Card([
            dcc.Graph(figure=g.abonnement(), className="graph"),
            dcc.Markdown(g.abonnement_string)

        ], className="card"),

        dbc.Card([
            html.Div([
                dcc.Markdown("Select ticker"),
                dcc.Dropdown(
                    g.ticker_data["ticker"].unique(),
                    "AMZN",
                    id="ticker_dropdown",
                )
            ]),
            dcc.Graph(figure={}, className="graph", id="ticker_graph"),
            dcc.Markdown(g.area_string)

        ], className="card")



    ])

])


@callback(
    Output("ticker_graph", "figure"),
    Input("ticker_dropdown", "value")
)

def update_graph(ticker):

    data = g.ticker_data
    data["date"] = pd.to_datetime(data["date"])
    data = data.set_index("date")

    data = data[data["ticker"] == ticker]

    fig = g.area(data)

    return fig
