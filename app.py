from dash import Dash, html, dcc, dash_table, Input, Output, State, callback_context
import plotly.express as px
import pandas as pd
import loggedin_user
import logout_user

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
usernames = ["5368", "1990", "3452", "akn", "akk", "av", "5883", "ap", "5839", 'aluebke', 'agg', '563', '8144', 'egan', 't0291',
             'cdv', '3851', 'CPP', '494', '288', '432', 'david17', '6872', 'dww', '5052', 't0185', 'ejj', '2427', 't0259', '7652', '7033', 'harold', 'hhm', 'iih', 'izz',
             '3211', 'inn', 'jbb', 'jit', 'JBee', 'jeg', 'jji', 'jerry', '1439', 'jmd', 't0039', '1971', '301', 'jjf', 'jll', 'jjl', 't0448', 'jes', '8899', 'kks', 'KNippes',
             '6323', '8131', 'llp', '7394', 'tz', 'mme', '7432', '6651', 't0289', 'mab', 'mth', '2662', 'mll', 'mam', 'milton', '4321', '2512', '4953', 't0048', 'pjl', 'rgg', 'ryh', 'rme',
             'rrg', 'rrs', '5178', 'rmd', 't0302', '5633', 'sll', '1460', 'svw', 'tap', 't0109', '8759', 'vaa', '????????????', 'vvt', "wjl"]

app.layout = html.Div(children=[
    html.H1(children='QT9 30min logout timer'),

    html.Div([
        html.Div(id='live-update-text'),
        dcc.Interval(
            id='one-min-checks',
            interval=1*1000,
            n_intervals=0
        )
    ]),

])


@app.callback(
    Output('live-update-text', 'children'),
    Input('one-min-checks', 'n_intervals')
)
def checkforloggedinusers(input_value):
    loggedinclient = loggedin_user.LoggedinUser()


if __name__ == '__main__':
    app.run_server(debug=True)
