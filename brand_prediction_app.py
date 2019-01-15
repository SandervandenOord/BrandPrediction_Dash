# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from utils import prediction_utils
from utils.dash_utils import row


app = dash.Dash(__name__)

server = app.server

colors = {
    'background': 'white',
    'text': 'blue',
}

app.layout = html.Div(
    children=[
        row([
            html.H2(
                'Predicting brand from a Beauty product title',
                style={'textAlign': 'center', 'color': colors['text']},
        )]),

        row([
            html.Br(),
            html.Label('Type a Beauty product title:'),
            dcc.Input(
                id='beauty_title',
                value='LOréal Paris X Isabel Marant Lippenstift - Limited Edition - 06 La Seine Shadow',
                type='text',
                size=100,
                minlength=5,
            ),
        ]),


        row([
            dcc.Graph(
                id='beauty_graph',
                config={
                    'displaylogo': False,  # don't show plotly logo
                    'modeBarButtonsToRemove': ['pan2d', 'lasso2d'],  # don't show certain options in plotly menu
                },
            ),
        ]),
    ],
)

@app.callback(
    Output('beauty_graph', 'figure'),
    [Input('beauty_title', 'value')]
)
def update_figure(beauty_title):
    predictions = prediction_utils.predict_top3_brands([beauty_title])

    brands = [predictions[brand_id]['brandname'] for brand_id in predictions.keys()]
    probabilities = [predictions[brand_id]['probability'] for brand_id in predictions.keys()]

    data = {
        'x': brands,
        'y': probabilities,
        'type': 'bar',
        'marker': {'color': 'blue'},
    }

    figure = {
         'data': [data],
         'layout': {
             'title': 'Predicted probabilities brands from title',
             'hovermode': 'closest',
             'plot_bgcolor': colors['background'],
             'paper_bgcolor': colors['background'],
             'font': {
                 'color': colors['text']
             },
             'xaxis': {
                 'title': 'Predicted brands',
             },
             'yaxis': {'title': 'P(X =x)'},
         },
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)



