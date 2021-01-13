# Import required libraries
import os
from random import randint

import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
## Need server=app.server for heroku https://dash.plotly.com/deployment
server = app.server


# Put your Dash code here
app.layout = html.Div(children= [
    html.H1("Header")
])



# Run the Dash app
if __name__ == '__main__':
    server.run(debug=True, threaded=True)
    # app.run_server(debug=True)
