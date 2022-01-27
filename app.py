import dash
from dash import Input, Output, State, html
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash_bootstrap_components as dbc
from numpy import sort
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
import pandas as pd

config = {'displayModeBar': False, "showTips": False, 'scrollZoom': False, 'responsive': False, 'staticPlot': False}

g1_fig = go.Figure()
g1_fig.add_trace(go.Bar(
    y=['YouTube United States', 'iTunes Canada', 'iTunes United States',
        'Amazon Video 2', 'Google Play Movie', 'iTunes Australia', 'Amazon Video 1'],
    x=[60, 70, 75, 80, 80, 90, 100],
    orientation='h',
    marker=dict(
        color='rgba(157, 158, 158, 1.0)'
    )
))
g1_fig.add_trace(go.Bar(
    y=['YouTube United States', 'iTunes Canada', 'iTunes United States',
        'Amazon Video 2', 'Google Play Movie', 'iTunes Australia', 'Amazon Video 1'],
    x=[0, 4, 3, 6, 9, 10, 8],
    orientation='h',
    marker=dict(
        color='rgba(200, 41, 87, 1.0)'
    )
))
g1_fig.update_layout(
    barmode='stack',
    height=250,
    plot_bgcolor='rgba(0,0,0,0)', 
    showlegend=False, 
    xaxis_visible=False, 
    xaxis_showticklabels=False, 
    margin=dict(l=20, r=20, t=20, b=20))

g2_fig = go.Figure()
g2_fig.add_trace(go.Bar(
    y=['Validated VOD', 'TV Everywhere', 'Free VOD',
        'Subscription VOD', 'Transaction VOD'],
    x=[5, 20, 85, 90, 100],
    orientation='h',
    marker=dict(
        color='rgba(200, 41, 87, 1.0)'
    )
))
g2_fig.update_layout(
    height=250, 
    plot_bgcolor='rgba(0,0,0,0)', 
    showlegend=False, 
    xaxis_visible=False, 
    xaxis_showticklabels=False, 
    margin=dict(l=20, r=20, t=20, b=20))

g3_fig = go.Figure()
g3_fig.add_trace(go.Bar(
    y=['Germany', 'Ireland', 'New Zealand', 'United Kingdom',
        'Canada', 'United States of America', 'Australia'],
    x=[40, 50, 55, 65, 70, 90, 100],
    orientation='h',
    marker=dict(
        color='rgba(143, 27, 77, 1.0)'
    )
))
g3_fig.update_layout(
    height=250,
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    xaxis_visible=False, 
    xaxis_showticklabels=False, 
    margin=dict(l=20, r=20, t=20, b=20))

g4_colors = ['rgb(217, 218, 218)', 'rgb(12, 34, 67)', 'rgb(106, 33, 69)',
             'rgb(153, 32, 69)', 'rgb(200, 31, 70)', 'rgb(213, 96, 109)', 'rgb(241, 205, 203)']
g4_labels = ['Others', 'Drama', 'Short',
             'Thriller', 'Romance', 'Documentary', 'Comedy']
g4_values = [3500, 2500, 1053, 900, 700, 900, 1200]
g4_fig = go.Figure(data=[go.Pie(
    labels=g4_labels,
    values=g4_values,
    hole=.5,
    marker_colors=g4_colors,
    textinfo='label+percent',
    textposition='outside')])
g4_fig.update_layout(
    height=250,
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=False,
    margin=dict(l=20, r=20, t=20, b=20))


g5_df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
g5_df['text'] = g5_df['airport'] + '' + g5_df['city'] + ', ' + \
g5_df['state'] + '' + 'Arrivals: ' + g5_df['cnt'].astype(str)
g5_fig = go.Figure(data=go.Scattergeo(
    lon=g5_df['long'],
    lat=g5_df['lat'],
    text=g5_df['text'],
    mode='markers',
    marker_color=g5_df['cnt'],
))
g5_fig.update_layout(
    geo=dict(
        scope='asia',
        showland=True,
        landcolor="rgb(143, 27, 77)",
        subunitcolor="rgb(213, 97, 110)",
        countrycolor="rgb(213, 97, 110)"
    ),
    height=250,
    margin=dict(l=20, r=20, t=20, b=20)
)


g6_categories = ['M45+', 'F<18', 'F18-29',
                 'F30-44', 'F45+', 'M<18', 'M18-29', 'M30-44']
g6_fig = go.Figure()
g6_fig.add_trace(go.Scatterpolar(
    r=[3, 5, 7.2, 9, 3, 5, 7.2, 9],
    theta=g6_categories,
    marker=dict(
        color='rgba(157, 158, 158, 1.0)'
    ),
    fill='toself',
    name="Average Affinity"
))
g6_fig.add_trace(go.Scatterpolar(
    r=[15, 26, 37, 45, 16, 25, 38, 45],
    theta=g6_categories,
    marker=dict(
        color='rgba(200, 41, 87, 1.0)'
    ),
    fill='toself',
    name="Contents affinity"
))


g6_fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=False
        )),
    height=250,
    plot_bgcolor='rgba(0,0,0,0)',
    showlegend=True,
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.1,
    xanchor="right",
    x=0.86
),
    margin=dict(l=20, r=20, t=20, b=20)
)

placement_selector = html.Div(
    [
        dbc.RadioItems(
            id="offcanvas-placement-selector",
            value="end",
        )
    ]
)
selection_canvas_buttons = dbc.ButtonGroup(
    [
        html.H5("CONTENTS", className="z_ml_10"),
        dbc.Button("Contents by Platform", className="z_s_c_button"),
        dbc.Button("Content Popularity", className="z_s_c_button"),
        dbc.Button("Producer Analysis", className="z_s_c_button"),
        dbc.Button("Price Analysis by Platfrom", className="z_s_c_button"),
        dbc.Button("Country Analysis", className="z_s_c_button"),
        dbc.Button("Content Evolution", className="z_s_c_button"),

        html.H5("PLATFORMS", className="z_ml_10"),
        dbc.Button("Platforms Contents Overlap", className="z_s_c_button"),
        dbc.Button("Platforms Affinity per Target", className="z_s_c_button"),
        dbc.Button("Ranker by Title Count", className="z_s_c_button"),
        dbc.Button("Content Renewal Rates", className="z_s_c_button"),
        dbc.Button("Platfroms available & planned", className="z_s_c_button"),
        dbc.Button("Methodology", className="z_s_c_button"),
    ],
    vertical=True,

)
selection_canvas = html.Div(
    [
        placement_selector,
        html.I(className="bi bi-justify", id="open-offcanvas_2", n_clicks=0),
        dbc.Offcanvas(
            html.P(
                selection_canvas_buttons
            ),
            id="offcanvas_2",
            title="MENU",
            is_open=False,
            className="z_s_canvas"
        ),
    ]
)
right_header = [
    dbc.Row([
        dbc.Col(width=3),
        dbc.Col(html.Div("Contents by Platform", className="z_mt_10"), width=5),
        dbc.Col(html.I(className="bi bi-funnel-fill"),
                width=2, className="z_right_header_icon"),
        dbc.Col(selection_canvas, width=2, className="z_right_header_icon"),
    ])

]
header = [
    dbc.Col(html.Div(html.Img(src="https://i.hizliresim.com/rjuk5uf.png",
            className="z_h_50")), className="z_header_bg", width=4),
    dbc.Col(html.Div(), className="z_header_bg", width=4),
    dbc.Col(html.Div(right_header), width=4, className="z_right_header"),
]


graph_1 = dbc.Card(
    [
        dbc.CardHeader("Contents by Platform",
                       className="text-start fw-bold bg-white z_graph_title_color z_graph_title_border "),
        dcc.Graph(figure=g1_fig, config=config)
    ],
    className="rounded-0 text-center shadow"
)
graph_2 = dbc.Card(
    [
        dbc.CardHeader("Contents by Package",
                       className="text-start fw-bold bg-white z_graph_title_color z_graph_title_border"),
        dcc.Graph(figure=g2_fig, config=config)
    ],
    className="rounded-0 text-center shadow"
)
graph_3 = dbc.Card(
    [
        dbc.CardHeader("Countries Where Content is Available",
                       className="text-start fw-bold bg-white z_graph_title_color z_graph_title_border"),
        dcc.Graph(figure=g3_fig, config=config)
    ],
    className="rounded-0 text-center shadow"
)
graph_4 = dbc.Card(
    [
        dbc.CardHeader(
            "Genres", className="text-start fw-bold bg-white z_graph_title_color z_graph_title_border"),
        dcc.Graph(figure=g4_fig, config=config)
    ],
    className="rounded-0 text-center shadow"
)
graph_5 = dbc.Card(
    [
        dbc.CardHeader(
            "Country of Orign", className="text-start fw-bold bg-white z_graph_title_color z_graph_title_border"),
        dcc.Graph(figure=g5_fig, config=config)
    ],
    className="rounded-0 text-center shadow"
)
graph_6 = dbc.Card(
    [
        dbc.CardHeader(
            "Content Affinity", className="text-start fw-bold bg-white z_graph_title_color z_graph_title_border"),
        dcc.Graph(figure=g6_fig, config=config)
    ],
    className="rounded-0 text-center shadow"
)

metric_1 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="https://i.hizliresim.com/gt8jhhl.png",
                             className="z_h_50"),
                    className="col-3",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H2(
                                "3.431", className="card-title text-center mb-0 z_metric_title_color"),
                            html.Small(
                                "Total Contents",
                                className="card-text text-muted text-center",
                            ),
                        ]
                    ),
                    className="col-md-8 text-center",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 border-0 z_metric"
)
metric_2 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="https://i.hizliresim.com/9m2f4w9.png",
                             className="z_h_50"),
                    className="col-3",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H2(
                                "2.405", className="card-title text-center mb-0 z_metric_title_color"),
                            html.Small(
                                "Movies",
                                className="card-text text-muted text-center",
                            ),
                        ]
                    ),
                    className="col-md-8 text-center",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 border-0 z_metric"
)
metric_3 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="https://i.hizliresim.com/e96lm94.png",
                             className="z_h_50"),
                    className="col-3",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H2(
                                "1.026", className="card-title text-center mb-0 z_metric_title_color"),
                            html.Small(
                                "Series",
                                className="card-text text-muted text-center",
                            ),
                        ]
                    ),
                    className="col-md-8 text-center",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 border-0 z_metric"
)
metric_4 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="https://i.hizliresim.com/38sokdp.png",
                             className="z_h_50"),
                    className="col-3",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H2(
                                "2.013", className="card-title text-center mb-0 z_metric_title_color"),
                            html.Small(
                                "Seasons",
                                className="card-text text-muted text-center",
                            ),
                        ]
                    ),
                    className="col-md-8 text-center",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 border-0 z_metric"
)
metric_5 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="https://i.hizliresim.com/f61wuha.png",
                             className="z_h_50"),
                    className="col-3",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H2(
                                "29.864", className="card-title text-center mb-0 z_metric_title_color"),
                            html.Small(
                                "Episodes",
                                className="card-text text-muted text-center",
                            ),
                        ]
                    ),
                    className="col-md-8 text-center",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 border-0 z_metric"
)
metric_6 = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(src="https://i.hizliresim.com/pglolhy.png",
                             className="z_h_50"),
                    className="col-3 ",
                ),
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.H2(
                                "20", className="card-title text-center mb-0 z_metric_title_color"),
                            html.Small(
                                "Relased in 2021",
                                className="card-text text-muted text-center",
                            ),
                        ]
                    ),
                    className="col-md-8 text-center",
                ),
            ],
            className="g-0 d-flex align-items-center",
        )
    ],
    className="mb-3 border-0 z_metric"
)

app = dash.Dash(external_stylesheets=[
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

app.layout = \
    html.Div([
        dbc.Row(
            header,
            justify="between",
        ),

        dbc.Row([
            dbc.Col([metric_1]),
            dbc.Col([metric_2]),
            dbc.Col([metric_3]),
            dbc.Col([metric_4]),
            dbc.Col([metric_5]),
            dbc.Col([metric_6]),
        ]),

        dbc.Row([
            dbc.Col(
                [graph_1], width=4),
            dbc.Col(
                [graph_2], width=4),
            dbc.Col(
                [graph_3], width=4),
        ]),
        html.Br(),
        dbc.Row([
            dbc.Col(
                [graph_4], width=4),
            dbc.Col(
                [graph_5], width=4),
            dbc.Col(
                [graph_6], width=4),
        ])
    ], className="z_container")


@app.callback(
    Output("offcanvas_2", "is_open"),
    Input("open-offcanvas_2", "n_clicks"),
    [State("offcanvas_2", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

@app.callback(
    Output("offcanvas_2", "placement"),
    Input("offcanvas-placement-selector", "value"),
)
def toggle_placement(placement):
    return placement


if __name__ == "__main__":
    app.run_server(debug=False, port=8050, host='localhost', use_reloader=True)
