import os
import dash
import base64
from PartNLP import Pipeline
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask import Flask, send_from_directory
from dash.dependencies import Input, Output, State

colors = {
    'background': '#111111',
    'text': '#7FDBFF',
    'red': '#FF338D ',
    'dark_read': '#AC0F0F',
    'blue': '#3336FF ',
    'fancy': '#45B7A4 ',
    'green': '#45B779',
    'black': '#403A3A',
    'black_dark': '#010101',
    'white': '#FFFEFE',
    'jaguar': '#28282D',
    'test': '#0E0F0F '
}
UPLOAD_DIRECTORY = os.path.dirname(os.path.realpath(__file__))


class Interface:
    def __init__(self):
        pass

    def run(self):
        if not os.path.exists(UPLOAD_DIRECTORY):
            os.makedirs(UPLOAD_DIRECTORY)

        server = Flask(__name__)
        app = dash.Dash(server=server)

        @server.route("/download/<path:path>")
        def download(path):
            """Serve a file from the upload directory."""
            return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

        external_stylesheets = [dbc.themes.BOOTSTRAP]
        app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

        app.layout = html.Div([
                html.Div([dbc.ButtonGroup([dbc.Button("ENGLISH"), dbc.Button("PERSIAN")],),
                          ], style={'float': 'right'}),

            html.Div([
                html.Span([
                    dbc.Badge("NATURAL LANGUAGE PROCESSING", color="info", className="mr-1"),
                    dbc.Badge("MACHINE LEARNING", color="primary", className="mr-1"),
                    dbc.Badge("PACKAGING", color="success", className="mr-1"),
                    dbc.Badge("Pip", color="danger", className="mr-1"),
                    dbc.Checklist(
                        options=[{'label': 'dark', "value": 1}],
                        value=[],
                        id="switches-input",
                        switch=True,
                    ),
                ]),
                html.H1('PPARSER PACKAGE', id='package_des', style={'textAlign': 'center', 'color': colors['green']}),

            ], style={'color': colors['white']}),

            html.Div([
                html.Div([dcc.Upload(id='upload-data',
                                     children=html.Div(['Drag and Drop or ',
                                                        html.A('Select Files')],
                                                       style={'textAlign': 'center', 'color': colors['green']}),
                                     style={
                                         'width': '30%',
                                         'height': '50px',
                                         'lineHeight': '60px',
                                         'borderWidth': '1px',
                                         'borderStyle': 'dashed',
                                         'borderRadius': '60px',
                                         'margin': '0 auto',
                                         'color': colors['green']
                                        },
                                     # Allow multiple files to be uploaded
                                     multiple=True
                                     ),
                    html.Div(id='output-data-upload'),
                          ], style={'margin': '10px'}),
                html.Div([
                        dbc.Button("Submit", id='SUBMIT', color="success", active=False, className="mr-1"),
                    ], style={'textAlign': 'center'}
                ),
            ]),

            html.Div([dbc.FormGroup(
            [
                dbc.Label("Packages"),
                dbc.RadioItems(
                    options=[
                        {"label": "HAZM", "value": 'HAZM'},
                        {"label": "PARSIVAR", "value": 'PARSIVAR'},
                        {'label': 'STANZA', 'value': 'STANZA'}
                    ],
                    value='STANZA',
                    id='package',
                    labelCheckedStyle={"color": "red"},
                    inline=True,
                ),
            ]
        )]),

            html.Div([
                html.Label('Operations'),
                dbc.Checklist(id="Operation",
                              options=[
                                  {'label': 'Word tokenize', 'value': 'W_TOKENIZE'},
                                  {'label': 'Sent tokenize', 'value': 'S_TOKENIZE'},
                                  {'label': 'Normalize', 'value': 'NORMALIZE'},
                                  {'label': 'Lemma', 'value': 'LEMMATIZE'},
                                  {'label': 'Stem', 'value': 'STEM'},
                              ],
                              labelCheckedStyle={"color": "red"}, value=['W_TOKENIZE'])
            ]),

            html.Div([
                html.Div([html.Div([dcc.Interval(id="progress-interval", n_intervals=0, interval=500),
                          dbc.Progress(id="progress", color='success')], style={
                                         'width': '50%',
                                         'height': '50px',
                                         'lineHeight': '60px',
                                         'margin': '0 auto',
                                        },
                                   ),
                          html.Div(dbc.Spinner(color="success"))], style={'textAlign': 'center', 'margin': '10px'}),
            ]),

            html.Div([
                    html.H2(['ABOUT PACKAGES'], style={'color': colors['green']}),
                    dbc.CardGroup(
                        [
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("HAZM", className="card-title", style={'color': colors['green']}),
                                        html.P(
                                            'HAZM is an open-source package designed for pre-processing Persian text.'
                                            'In its website you can find many useful examples of its usage.',
                                            className="card-text",
                                        ),
                                        dbc.Button(
                                            "Learn More", color="danger", className="mt-auto",
                                            href='http://www.sobhe.ir/hazm/'
                                        ),
                                    ]
                                ), color="success", outline=True,
                            ),
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("STANZA", className="card-title", style={'color': colors['green']}),
                                        html.P(
                                            'STANZA is a famous open-source package presented by Standford university.'
                                            'It is very powerful because of its flexibilities. Multilingual, run on'
                                            'GPU are just a few examples of its power. You can check it '
                                            'out through the button.',
                                            className="card-text",
                                        ),
                                        dbc.Button(
                                            "Learn More", color="danger", className="mt-auto",
                                            href='https://github.com/stanfordnlp/stanza/'
                                        ),
                                    ]
                                ), color="success", outline=True,
                            ),
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5("PARSIVAR", className="card-title", style={'color': colors['green']}),
                                        html.P('PARSIVAR is a well-known per-processing package for Persian language.'
                                               'It used as a per-processor tool in many projects in Farsi.'
                                               'You can check its all possible operations by clicking Learn More button.',
                                               className="card-text",
                                               ),
                                        dbc.Button(
                                            "Learn More", color="danger", className="mt-auto",
                                            href='https://github.com/ICTRC/Parsivar'
                                        ),
                                    ]
                                ), color="success", outline=True,
                            ),
                        ]
                    ),

                    html.Div([
                        html.H2(dbc.Jumbotron(
                            [
                                html.H4("WHAT IS PPARSER?", className="display-3", style={'color': colors['green']}),
                                html.Hr(className="my-2"),
                                html.P('PParser is an integrated package for pre-processing purposes.'),
                                html.Div(
                                    html.Div([
                                        dbc.Button("Learn More", id="open-body-scroll", color='success'),
                                        dbc.Modal(
                                            [
                                                dbc.ModalHeader("PPARSER", style={'color': colors['green']}),
                                                dbc.ModalBody('PPARSER is an integrated package. It aims to '
                                                              'save the time of developers by '
                                                              'automatization of pre-processing. '
                                                              'It uses many famous packages to reach its goal. '
                                                              'Moreover, PParser supports two '
                                                              'languages English and Persian so far. '
                                                              'With PParser all thing you '
                                                              'need to do is select the language of '
                                                              'the text you want to pre-process it and then '
                                                              'you should select the operation you intend to '
                                                              'do let say word_tokenize and that is it!'
                                                              'PParser does all steps it needs for pre-processing. '),
                                                dbc.ModalFooter(
                                                    dbc.Button(
                                                        "Close", id="close-body-scroll", className="ml-auto"
                                                    )
                                                ),
                                            ],
                                            id="modal-body-scroll",
                                            scrollable=True,
                                        ),
                                    ]),
                                ),
                            ]
                        ), style={'backgroundColor': colors['green']}),
                    ]),

                dbc.Toast(
                    [html.H6('The preprocessed file has been saved in {}'.format(UPLOAD_DIRECTORY + 'output.json'), className="mb-0")],
                    header='Info', id='RESULT', icon="success", duration=8000, style={"position": "fixed", "top": 200,
                                                                                      "right": 200, "width": 2000, 'color': colors['green']}
                )

            ], style={'textAlign': 'center'}),
        ], style={'backgroundColor': colors['test']})

        @app.callback(
            [Output("progress", "value"), Output("progress", "children")],
            [Input("progress-interval", "n_intervals")],
        )
        def update_progress(n):
            # check progress of some background process, in this example we'll just
            # use n_intervals constrained to be in 0-100
            progress = min(n % 110, 100)
            # only add text after 5% progress to ensure text isn't squashed too much
            return progress, f"{progress} %" if progress >= 5 else ""

        def toggle_modal(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open

        app.callback(
            Output("modal-body-scroll", "children"),
            [
                Input("open-body-scroll", "n_clicks"),
                Input("close-body-scroll", "n_clicks"),
            ],
            [State("modal-body-scroll", "is_open")],)(toggle_modal)

        def save_file(name, content):
            """Decode and store a file uploaded with Plotly Dash."""
            content_type, content_string = content.split(',')
            decoded = base64.b64decode(content_string)
            return decoded.decode('utf-8')

        @app.callback(
            Output('RESULT', 'is_open'),
            [Input(component_id='SUBMIT', component_property='n_clicks')],
            state=[State("upload-data", "filename"), State("upload-data", "contents"),
                   State('package', 'value'), State('Operation', 'value')])
        def update_output(n_clicks, filename, contents, package, operation):
            if filename is not None and contents is not None:
                for name, data in zip(filename, contents):
                    contents = save_file(name, data)
                    pre_process_data(package, operation, contents)
                    return True
            else:
                return False

        def pre_process_data(package, operations, data):
            Pipeline(lang='Persian', package=package, processors=operations, text=data)
        app.run_server(debug=True)

