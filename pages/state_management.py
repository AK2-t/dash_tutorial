import dash
from dash import html, dcc, callback, Input, Output, State, ctx, ALL, MATCH
import json

# Register this page in the app
dash.register_page(
    __name__, 
    path='/state-management',
    name="状態管理", 
    order=3
)

# Define the layout for this page
layout = html.Div([
    html.Div([
        html.H2("Dashにおける状態管理", className="card-title"),
        html.P("このページでは、Dashアプリケーションで状態を管理するさまざまな方法を紹介します。"),
    ], className="card"),
    
    # Basic State Example
    html.Div([
        html.H2("基本的な状態の例", className="card-title"),
        html.P("この例では、コールバックをトリガーせずに入力値を取得するために、Stateオブジェクトを使用する方法を紹介します。"),
        
        html.Div([
            html.Label("テキストを入力してください："),
            dcc.Input(
                id='basic-state-input',
                type='text',
                value='',
                placeholder='何か入力してください...',
                style={'width': '100%', 'marginBottom': '10px'}
            ),
            
            html.Button('送信', id='basic-state-button', n_clicks=0,
                      style={'marginTop': '10px', 'marginBottom': '20px', 'padding': '10px 20px'}),
            
            html.Div(id='basic-state-output')
        ])
    ], className="card"),
    
    # Store Component Example
    html.Div([
        html.H2("Storeコンポーネントの例", className="card-title"),
        html.P("この例では、コールバック間で状態を維持するためにdcc.Storeコンポーネントを使用する方法を紹介します。"),
        
        html.Div([
            # Hidden div to store the data
            dcc.Store(id='store-example', storage_type='memory'),
            
            html.Label("保存する値を入力してください："),
            dcc.Input(
                id='store-input',
                type='text',
                value='',
                placeholder='保存する値を入力してください...',
                style={'width': '100%', 'marginBottom': '10px'}
            ),
            
            html.Button('ストアに保存', id='store-button', n_clicks=0,
                      style={'marginTop': '10px', 'marginBottom': '20px', 'padding': '10px 20px'}),
            
            html.Div(id='store-output'),
            
            html.Hr(),
            
            html.Label("保存された値："),
            html.Div(id='stored-values-display')
        ])
    ], className="card"),
    
    # Callback Context Example
    html.Div([
        html.H2("コールバックコンテキストの例", className="card-title"),
        html.P("この例では、どの入力がコールバックをトリガーしたかを判断するためにコールバックコンテキストを使用する方法を紹介します。"),
        
        html.Div([
            html.Button('ボタン 1', id='ctx-button-1', n_clicks=0,
                      style={'marginRight': '10px', 'padding': '10px 20px'}),
            html.Button('ボタン 2', id='ctx-button-2', n_clicks=0,
                      style={'marginRight': '10px', 'padding': '10px 20px'}),
            html.Button('ボタン 3', id='ctx-button-3', n_clicks=0,
                      style={'padding': '10px 20px'}),
            
            html.Div(id='ctx-output', style={'marginTop': '20px'})
        ])
    ], className="card"),
    
    # Pattern-Matching Callbacks Example
    html.Div([
        html.H2("パターンマッチングコールバック", className="card-title"),
        html.P("この例では、動的なUI要素を処理するためにパターンマッチングコールバックを使用する方法を紹介します。"),
        
        html.Div([
            html.Button('アイテムを追加', id='add-item-button', n_clicks=0,
                      style={'marginBottom': '20px', 'padding': '10px 20px'}),
            
            html.Div(id='dynamic-item-container', children=[]),
            
            html.Hr(),
            
            html.Label("選択された値："),
            html.Div(id='dynamic-output')
        ])
    ], className="card"),
    
    # Clientside Callbacks Example
    html.Div([
        html.H2("クライアントサイドコールバック", className="card-title"),
        html.P("この例では、パフォーマンスを向上させるためのクライアントサイドコールバックの使用方法を紹介します。"),
        
        html.Div([
            html.Label("スライダー値："),
            html.Div([
                dcc.Slider(
                    id='clientside-slider',
                    min=0,
                    max=100,
                    step=1,
                    value=50,
                    marks={0: '0', 25: '25', 50: '50', 75: '75', 100: '100'},
                    tooltip={"placement": "bottom", "always_visible": True}
                )
            ], style={'marginBottom': '20px'}),
            
            html.Div(id='clientside-output')
        ])
    ], className="card")
])

# Register clientside callback
clientside_callback = """
function(value) {
    return 'スライダー値: ' + value + ' (クライアントサイドコールバックで更新)';
}
"""

# Apply the clientside callback
app = dash.get_app()
app.clientside_callback(
    clientside_callback,
    Output('clientside-output', 'children'),
    Input('clientside-slider', 'value')
)

# Basic State Example Callback
@callback(
    Output('basic-state-output', 'children'),
    Input('basic-state-button', 'n_clicks'),
    State('basic-state-input', 'value'),
    prevent_initial_call=True
)
def update_basic_state_output(n_clicks, input_value):
    if n_clicks == 0:
        return "値を表示するには送信を押してください。"
    
    return html.Div([
        html.P(f"ボタンは{n_clicks}回クリックされました。"),
        html.P(f"入力値は: {input_value}")
    ])

# Store Component Example Callbacks
@callback(
    Output('store-example', 'data'),
    Input('store-button', 'n_clicks'),
    State('store-input', 'value'),
    State('store-example', 'data'),
    prevent_initial_call=True
)
def save_to_store(n_clicks, input_value, current_data):
    if not input_value:
        return current_data or {"items": []}
    
    if current_data is None:
        current_data = {"items": []}
        
    current_data["items"] = current_data.get("items", []) + [input_value]
    
    return current_data

@callback(
    Output('store-output', 'children'),
    Input('store-example', 'data')
)
def update_store_output(data):
    if not data:
        return "まだデータが保存されていません。"
    
    return f"正常に保存されました！ 合計アイテム数: {len(data.get('items', []))}"

@callback(
    Output('stored-values-display', 'children'),
    Input('store-example', 'data')
)
def display_stored_values(data):
    if not data or not data.get('items', []):
        return "まだ値が保存されていません。"
    
    items = data.get('items', [])
    return html.Ul([html.Li(item) for item in items])

# Callback Context Example
@callback(
    Output('ctx-output', 'children'),
    Input('ctx-button-1', 'n_clicks'),
    Input('ctx-button-2', 'n_clicks'),
    Input('ctx-button-3', 'n_clicks'),
    prevent_initial_call=True
)
def update_ctx_output(btn1, btn2, btn3):
    button_id = ctx.triggered_id
    button_value = ctx.triggered[0]['value']
    
    return html.Div([
        html.P(f"コールバックをトリガーしたボタン: {button_id}"),
        html.P(f"現在の値 (n_clicks): {button_value}"),
        html.P("すべてのボタンの値:"),
        html.Ul([
            html.Li(f"ボタン 1: {btn1}"),
            html.Li(f"ボタン 2: {btn2}"),
            html.Li(f"ボタン 3: {btn3}")
        ])
    ])

# Pattern-Matching Callbacks Example
@callback(
    Output('dynamic-item-container', 'children'),
    Input('add-item-button', 'n_clicks'),
    State('dynamic-item-container', 'children'),
    prevent_initial_call=True
)
def add_dynamic_item(n_clicks, current_children):
    if n_clicks == 0:
        return current_children
    
    new_item_id = n_clicks if current_children is None else len(current_children) + 1
    
    new_item = html.Div([
        dcc.Input(
            id={
                'type': 'dynamic-input',
                'index': new_item_id
            },
            type='text',
            placeholder=f'アイテム {new_item_id}',
            style={'marginRight': '10px'}
        ),
        html.Button(
            '選択',
            id={
                'type': 'dynamic-button',
                'index': new_item_id
            },
            n_clicks=0,
            style={'padding': '5px 10px'}
        )
    ], style={'margin': '5px 0'})
    
    return current_children + [new_item] if current_children else [new_item]

@callback(
    Output('dynamic-output', 'children'),
    Input({'type': 'dynamic-button', 'index': ALL}, 'n_clicks'),
    State({'type': 'dynamic-input', 'index': ALL}, 'value'),
    prevent_initial_call=True
)
def update_dynamic_output(button_clicks, input_values):
    # Get the button that was clicked
    triggered_id = ctx.triggered_id
    if triggered_id is None:
        return "まだ選択されていません。"
    
    # Get the index of the button that was clicked
    index = triggered_id['index']
    
    # Find the corresponding input value
    input_index = [i for i, item in enumerate(ctx.inputs_list[0]) if item['id']['index'] == index][0]
    value = input_values[input_index] or "値が入力されていません"
    
    return html.Div([
        html.P(f"選択されたアイテム {index}: {value}"),
        html.P("すべての値:"),
        html.Pre(json.dumps(
            {f"Item {i+1}": val for i, val in enumerate(input_values) if val}, 
            indent=2
        ))
    ])