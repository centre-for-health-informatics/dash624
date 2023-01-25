#!/usr/bin/env python3

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


def load_data(url):
    """
    Load data from a shared google drive csv
    :param url: the shared url string
    :returns: a pandas dataframe
    """
    file_id = url.split("/")[-2]
    dwn_url = "https://drive.google.com/uc?id=" + file_id
    df = pd.read_csv(dwn_url)
    return df


url = "***REPLACE ME WITH SHARED URL***"
df = load_data(url)

# Create our first figure
fig = px.box(df, x="WBC", color="SepsisLabel")

# Style the figure
fig.update_layout(
    title="White Blood Count and Sepsis",
    font_size=22,
)

app.layout = html.Div(
    [
        html.H1("Lecture 3 -- Distributions"),
        """
        Let's explore the sepsis data!

        Not the best styling so hopefully you can improve it.
        The code shows some parameters you can manipulate, but there are lots more to try!
        """,
        dcc.Graph(
            figure=fig,
            style={
                "width": "80%",
                "height": "70vh",
            },
            id="OurFirstFigure",
        ),
        dcc.Graph(
            figure=fig,
            style={
                "width": "100%",
                "height": "50vh",
            },
        ),
        dcc.Graph(
            figure=fig,
            style={
                "width": "40vh",
                "height": "40vh",
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=False)
