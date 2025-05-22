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
    
    # Bootstrap Components
    html.Div([
        html.H2("Bootstrapコンポーネント", className="card-title"),
        html.P("これらのコンポーネントはdash-bootstrap-componentsライブラリを必要とします。"),
        
        html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("カードタイトル"),
                        dbc.CardBody([
                            html.H5("カード見出し", className="card-title"),
                            html.P("これはDashでのBootstrapカードコンポーネントのデモです。", className="card-text"),
                            dbc.Button("クリック", color="primary", id="card-button")
                        ])
                    ])
                ], width=6),
                
                dbc.Col([
                    dbc.Alert("これはプライマリアラートです", color="primary"),
                    dbc.Alert("これはセカンダリアラートです", color="secondary"),
                    dbc.Alert("これは成功アラートです", color="success"),
                    dbc.Progress(value=75, style={"height": "30px", "marginBottom": "10px"}),
                    dbc.ButtonGroup([
                        dbc.Button("左", color="primary"),
                        dbc.Button("中央", color="secondary"),
                        dbc.Button("右", color="success")
                    ])
                ], width=6)
            ]),
            
            html.Div(style={"height": "20px"}),
            
            dbc.Row([
                dbc.Col([
                    dbc.Tabs([
                        dbc.Tab(html.P("これはタブ1の内容です"), label="タブ 1"),
                        dbc.Tab(html.P("これはタブ2の内容です"), label="タブ 2"),
                        dbc.Tab(html.P("これはタブ3の内容です"), label="タブ 3")
                    ])
                ], width=12)
            ])
        ])
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