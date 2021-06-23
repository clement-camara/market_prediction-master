import pandas as pd
from plotly.subplots import make_subplots
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import plotly.graph_objects as go
import dash_core_components as dcc

df = pd.read_csv('data_market_final.csv')

#print(df.columns)


# create dash app with bootstrap feature
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Create figure with secondary y-axis
def strategy(fig):
    # Add traces
    fig.add_trace(
        go.Scatter(x=df.Date, y=df.Close, name="Close NASDAQ 1008€"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df.Date, y=df.MM_pf, name="Stratégie NASDAQ MM 150 période "),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df.Date, y=df.VIX_pf, name="Stratégie VIX MM 100 périodes"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df.Date, y=df.RSI100_pf, name="Stratégie RSI MM STD avec 100 périodes"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df.Date, y=df.supermodel_pf, name="Stratégie cumul des models sans frais"),
        secondary_y=False,
    )
    fig.add_trace(
        go.Scatter(x=df.Date, y=df.supermodel_pf_frais, name="Stratégie cumul des models avec frais"),
        secondary_y=False,
    )


fig2 = make_subplots(specs=[[{"secondary_y": True}]])


def indicator_graph(fig2):
    fig2.add_trace(
        go.Scatter(x=df.Date, y=df.Close, name="Close NASDAQ 1008€"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df.Date, y=df.MM_indicator, name="Indicateur du NASDAQ MM"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df.Date, y=df.VIX_indicator * 56.5, name="Indicateur VIX"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df.Date, y=df.GAFA_indicator * 4500, name="Indicateur des GAFA"),
        secondary_y=False,
    )
    fig2.add_trace(
        go.Scatter(x=df.Date, y=df.vol_indicator / 400000, name="Indicateur du volume NASDAQ"),
        secondary_y=False,
    )



indicator_graph(fig2)
fig = make_subplots(specs=[[{"secondary_y": True}]])


def display_graph(fig):
    # Set x-axis title
    fig.update_xaxes(title_text="Dates")
    # Set y-axes titles
    fig.update_yaxes(title_text="<b> yaxis Volumes scale </b>", secondary_y=False)
    fig.update_yaxes(title_text="<b> yaxis Vix Scale </b>", secondary_y=True)
    fig.update_layout(title_text="Switching between linear and log yaxis ",
                      updatemenus=[
                          dict(
                              buttons=[
                                  dict(label="Linear",
                                       method="relayout",
                                       args=[{"yaxis.type": "linear"}]),
                                  dict(label="Log",
                                       method="relayout",
                                       args=[{"yaxis.type": "log"}]),
                              ])]
                      );


display_graph(fig)
strategy(fig)

display_graph(fig2)

app.layout = html.Div([
    # top container
    html.Header(
        html.H3('Projet sur la finance'),
        className="bg-light text-center py-4",
    ),
    html.Div(className='container',
             children=[
                 html.H3(""),
                 dbc.Row([
                     dcc.Graph(
                         id='graph1',
                         style={
                             'height': 500,
                             'width': '100%',
                             'display': 'inline-block'
                         },
                         figure=fig
                     ), ]),
                 dbc.Row([
                     dcc.Graph(
                         figure=fig2,
                         style={
                             'height': 500,
                             'width': '100%',
                             'display': 'inline-block'}, )
                 ])
             ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
