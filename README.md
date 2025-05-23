# Dashについて

Pythonを用いたwebフレームワーク

## Reactに対するDashの利点

・環境構築が楽
・pandasやnumpy、sklearn、plotlyなどのライブラリを使えるので、機械学習系のデータ表示に便利
→とっつきやすさ、データ分析とのシナジーが魅力

## Dashの欠点

・コードのメンテ性があまり良くない
・複雑なUIは向いてない
→大規模アプリには向いておらず、モックや簡単なアプリに向いてる

## Dashにおける状態管理

### 基本

Dash: コンポーネント自体が値を持つ
dcc.Input(id='my-input', value='初期値')  # コンポーネント自体に値が入ってる

idは、コンポーネントの識別子

コールバック関数とInput,Output,Stateによって状態管理を実現する。

コールバック関数：@app.callback
Inputに指定したコンポーネントのプロパティが変化した時に実行される。

```python
import dash
from dash import dcc, html, Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='name-input', placeholder='名前を入力'),
    html.Button('送信', id='submit-btn', n_clicks=0),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),       # 出力先：どこを更新するか
    Input('submit-btn', 'n_clicks'),    # 入力元：何をきっかけにするか
    State('name-input', 'value')        # 状態：値を取得するだけ
)
def update_output(n_clicks, name):
    if n_clicks > 0 and name:
        return f'こんにちは、{name}さん！'
    return 'ボタンを押してください'
```

OutputとInputとStateの役割
Output: 「どこに結果を表示するか」を指定

Output('コンポーネントID', 'プロパティ名')
例：Output('output', 'children') → outputの中身を更新

Input: 「何をきっかけに実行するか」を指定

Input('コンポーネントID', 'プロパティ名')
例：Input('submit-btn', 'n_clicks') → ボタンクリックで実行

State: 「値を取得するだけ」を指定

State('コンポーネントID', 'プロパティ名')
例：State('name-input', 'value') → 値が変わってもコールバック実行されない

## Dashのディレクトリ構造

`pages`ディレクトリで定義されたページに自動でルーティングが設定される。

ディレクトリ構造の例:
```
app.py
pages/
├── __init__.py
├── home.py
├── page1.py
└── page2.py
```

app.pyでの設定例:
```python
import dash
from dash import Dash, html

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('マルチページDashアプリケーション'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## UIコンポーネントライブラリ

Dashにはいくつかのコンポーネントライブラリがある。

主に使うのは以下の2つ
dash-bootstrap-components：一番古参。AIに書かせると、基本はこれを使う 
dash-mantine-components:割と新しい。個人的に好き

## データ分析ライブラリとの統合

Dashは、以下のようなPythonのデータサイエンス系エコシステムを利用できる。
Plotlyで作成したグラフ等はそのまま画面に出すことができる。

・NumPy 
・Pandas
・Plotly
・Scikit
・SciPy
・Statsmodels

```python
import dash
from dash import dcc, html, Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2('インタラクティブ回帰分析'),
    
    html.Label('データ数:'),
    dcc.Slider(id='data-size', min=50, max=500, step=50, value=100),
    
    html.Label('ノイズレベル:'),
    dcc.Slider(id='noise-level', min=0.1, max=2.0, step=0.1, value=0.5),
    
    dcc.Graph(id='regression-plot'),
    html.Div(id='stats')
])

@app.callback(
    [Output('regression-plot', 'figure'),
     Output('stats', 'children')],
    [Input('data-size', 'value'),
     Input('noise-level', 'value')]
)
def update_analysis(n_samples, noise):
    # NumPy: データ生成
    np.random.seed(42)
    X = np.random.uniform(0, 10, n_samples)
    y = 2 * X + 1 + np.random.normal(0, noise, n_samples)
    
    # Pandas: DataFrame作成
    df = pd.DataFrame({'X': X, 'y': y})
    
    # Scikit-learn: 線形回帰
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))
    r2 = r2_score(y, y_pred)
    
    # Plotly: グラフ作成
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=X, y=y, mode='markers', name='データ'))
    fig.add_trace(go.Scatter(x=X, y=y_pred, mode='lines', name='回帰線'))
    fig.update_layout(title='線形回帰分析', xaxis_title='X', yaxis_title='y')
    
    # 統計情報
    stats = html.Div([
        html.P(f'データ数: {n_samples}'),
        html.P(f'回帰係数: {model.coef_[0]:.2f}'),
        html.P(f'切片: {model.intercept_:.2f}'),
        html.P(f'決定係数 (R²): {r2:.3f}')
    ])
    
    return fig, stats

if __name__ == '__main__':
    app.run_server(debug=True)
```

## AIに書かせる時のtips

duplicate callbackによるエラーがよく起こる。
私は以下のようなプロンプトを注意事項として与えることが多い。
