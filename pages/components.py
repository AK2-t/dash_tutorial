import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc

# Register this page in the app
dash.register_page(__name__, name="UIコンポーネント", order=1)

# Define the layout for this page
layout = html.Div([
    html.Div([
        html.H2("UIコンポーネント", className="card-title"),
        html.P("このページではDashで利用可能な様々なUIコンポーネントを紹介しています。"),
    ], className="card"),
    
    # Basic Input Components
    html.Div([
        html.H2("基本的な入力コンポーネント", className="card-title"),
        
        html.Div([
            html.Label("テキスト入力"),
            dcc.Input(
                id='text-input-demo',
                type='text',
                placeholder='Enter some text...',
                value='',
                style={'width': '100%', 'marginBottom': '10px'}
            ),
            
            html.Label("数値入力"),
            dcc.Input(
                id='numeric-input-demo',
                type='number',
                placeholder='Enter a number...',
                value=0,
                min=0,
                max=100,
                step=1,
                style={'width': '100%', 'marginBottom': '10px'}
            ),
            
            html.Label("ドロップダウン"),
            dcc.Dropdown(
                id='dropdown-demo',
                options=[
                    {'label': 'オプション 1', 'value': 'opt1'},
                    {'label': 'オプション 2', 'value': 'opt2'},
                    {'label': 'オプション 3', 'value': 'opt3'}
                ],
                value='opt1',
                style={'marginBottom': '10px'}
            ),
            
            html.Label("複数選択ドロップダウン"),
            dcc.Dropdown(
                id='multi-dropdown-demo',
                options=[
                    {'label': 'オプション 1', 'value': 'opt1'},
                    {'label': 'オプション 2', 'value': 'opt2'},
                    {'label': 'オプション 3', 'value': 'opt3'}
                ],
                multi=True,
                value=['opt1'],
                style={'marginBottom': '10px'}
            ),
            
            html.Label("スライダー"),
            html.Div([
                dcc.Slider(
                    id='slider-demo',
                    min=0,
                    max=100,
                    step=1,
                    value=50,
                    marks={0: '0', 25: '25', 50: '50', 75: '75', 100: '100'},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], style={'marginBottom': '20px'}),
            
            html.Label("レンジスライダー"),
            html.Div([
                dcc.RangeSlider(
                    id='range-slider-demo',
                    min=0,
                    max=100,
                    step=1,
                    value=[25, 75],
                    marks={0: '0', 25: '25', 50: '50', 75: '75', 100: '100'},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], style={'marginBottom': '20px'}),
            
            html.Label("チェックリスト"),
            dcc.Checklist(
                id='checklist-demo',
                options=[
                    {'label': ' オプション 1', 'value': 'opt1'},
                    {'label': ' オプション 2', 'value': 'opt2'},
                    {'label': ' オプション 3', 'value': 'opt3'}
                ],
                value=['opt1', 'opt3'],
                style={'marginBottom': '10px'}
            ),
            
            html.Label("ラジオボタン"),
            dcc.RadioItems(
                id='radio-demo',
                options=[
                    {'label': ' オプション 1', 'value': 'opt1'},
                    {'label': ' オプション 2', 'value': 'opt2'},
                    {'label': ' オプション 3', 'value': 'opt3'}
                ],
                value='opt1',
                style={'marginBottom': '10px'}
            ),
            
            html.Label("日付選択"),
            dcc.DatePickerSingle(
                id='date-picker-demo',
                date='2023-01-01',
                style={'marginBottom': '10px'}
            ),
            
            html.Label("日付範囲選択"),
            dcc.DatePickerRange(
                id='date-range-demo',
                start_date='2023-01-01',
                end_date='2023-01-31',
                style={'marginBottom': '20px'}
            ),
            
            html.Label("テキストエリア"),
            dcc.Textarea(
                id='textarea-demo',
                value='Enter text here...',
                style={'width': '100%', 'height': 100, 'marginBottom': '20px'}
            ),
            
            html.Label("ファイルアップロード"),
            dcc.Upload(
                id='upload-demo',
                children=html.Div([
                    'ドラッグアンドドロップまたは ',
                    html.A('ファイル選択')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'marginBottom': '20px'
                },
                multiple=True
            ),
            
            html.Button('送信', id='submit-button-demo', n_clicks=0,
                      style={'marginTop': '10px', 'padding': '10px 20px'})
        ])
    ], className="card"),
    
    # Component Demo Output
    html.Div([
        html.H2("コンポーネントインタラクションデモ", className="card-title"),
        html.Div(id='components-demo-output')
    ], className="card"),
    
    # Framework Comparison Section - Title
    html.Div([
        html.H2("UIフレームワーク比較", className="card-title"),
        html.P("同じUIを異なるスタイルのBootstrapで実装した比較です。"),
        
        # Two-column layout for comparison
        html.Div([
            # Left column - Bootstrap
            html.Div([
                html.H3("Bootstrap実装", style={"textAlign": "center"}),
                html.Hr(),
                
                # Card with title, text and button
                dbc.Card([
                    dbc.CardHeader("カードの例"),
                    dbc.CardBody([
                        html.H5("カードタイトル", className="card-title"),
                        html.P("これはカードの内容です。Bootstrap UIを使っています。", className="card-text"),
                        dbc.Button("ボタン", color="primary", id="bs-card-button")
                    ])
                ], className="mb-4"),
                
                # Form elements
                dbc.Form([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("テキスト入力"),
                            dbc.Input(type="text", placeholder="テキストを入力...", id="bs-text-input")
                        ], className="mb-3"),
                    ]),
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("セレクト"),
                            dbc.Select(
                                id="bs-select",
                                options=[
                                    {"label": "オプション 1", "value": "1"},
                                    {"label": "オプション 2", "value": "2"},
                                    {"label": "オプション 3", "value": "3"},
                                ],
                                value="1"
                            )
                        ], className="mb-3"),
                    ]),
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("チェックボックス"),
                            dbc.Checkbox(id="bs-checkbox", label="同意する", value=False)
                        ], className="mb-3"),
                    ]),
                    
                    dbc.Button("送信", color="success", id="bs-submit")
                ])
            ], style={"width": "48%", "float": "left"}),
            
            # Right column - Dash Bootstrap
            html.Div([
                html.H3("Dash Bootstrap実装（右側）", style={"textAlign": "center"}),
                html.Hr(),
                
                # Card with title, text and button
                dbc.Card([
                    dbc.CardHeader("カードの例"),
                    dbc.CardBody([
                        html.H5("カードタイトル", className="card-title"),
                        html.P("これはカードの内容です。Dash Bootstrap UIを使っています。", className="card-text"),
                        dbc.Button("ボタン", color="primary", id="bs-card-button-2")
                    ])
                ], className="mb-4"),
                
                # Form elements
                dbc.Form([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("テキスト入力"),
                            dbc.Input(type="text", placeholder="テキストを入力...", id="bs-text-input-2")
                        ], className="mb-3"),
                    ]),
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("セレクト"),
                            dbc.Select(
                                id="bs-select-2",
                                options=[
                                    {"label": "オプション 1", "value": "1"},
                                    {"label": "オプション 2", "value": "2"},
                                    {"label": "オプション 3", "value": "3"},
                                ],
                                value="1"
                            )
                        ], className="mb-3"),
                    ]),
                    
                    dbc.Row([
                        dbc.Col([
                            dbc.Label("チェックボックス"),
                            dbc.Checkbox(id="bs-checkbox-2", label="同意する", value=False)
                        ], className="mb-3"),
                    ]),
                    
                    dbc.Button("送信", color="success", id="bs-submit-2")
                ])
            ], style={"width": "48%", "float": "right"})
        ], style={"display": "flex", "justifyContent": "space-between"})
    ], className="card")
])

# Callbacks for the demo
@callback(
    Output('components-demo-output', 'children'),
    Input('submit-button-demo', 'n_clicks'),
    State('text-input-demo', 'value'),
    State('dropdown-demo', 'value'),
    State('slider-demo', 'value'),
    State('checklist-demo', 'value'),
    prevent_initial_call=True
)
def update_demo_output(n_clicks, text_value, dropdown_value, slider_value, checklist_value):
    if n_clicks == 0:
        return "コンポーネントの値を表示するには送信を押してください。"
    
    return html.Div([
        html.P(f"送信ボタンが{n_clicks}回クリックされました"),
        html.P(f"テキスト入力値: {text_value}"),
        html.P(f"ドロップダウン選択: {dropdown_value}"),
        html.P(f"スライダー値: {slider_value}"),
        html.P(f"チェックリスト選択: {checklist_value}")
    ])

# Callback for Bootstrap form submission
@callback(
    Output('bs-submit', 'children'),
    Input('bs-submit', 'n_clicks'),
    State('bs-text-input', 'value'),
    State('bs-select', 'value'),
    State('bs-checkbox', 'value'),
    prevent_initial_call=True
)
def bs_form_submit(n_clicks, text, select, checkbox):
    return f"送信済み ({n_clicks})"

# Callback for Bootstrap form submission (right side)
@callback(
    Output('bs-submit-2', 'children'),
    Input('bs-submit-2', 'n_clicks'),
    State('bs-text-input-2', 'value'),
    State('bs-select-2', 'value'),
    State('bs-checkbox-2', 'value'),
    prevent_initial_call=True
)
def bs_form_submit_2(n_clicks, text, select, checkbox):
    return f"送信済み ({n_clicks})"