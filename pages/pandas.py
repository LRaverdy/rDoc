import dash
import pandas as pd
import numpy as np
from dash import dcc, html, Input, Output, callback, dash_table
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc


dash.register_page(__name__, path='/pandas')


layout = html.Div([

], className="fill-space")