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

### Reactとの違い

**React**: `useState` + `useEffect` でコンポーネント内の状態管理  
**Dash**: `@app.callback` でアプリ全体の状態管理

### Input,Output

```python
import dash
from dash import dcc, html, Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='text-input', placeholder='入力してください'),
    html.Div(id='text-output')
])

@app.callback(
    Output('text-output', 'children'),  # 出力先：どこを更新するか
    Input('text-input', 'value')        # 入力元：何をきっかけにするか
)
def update_text(input_value):
    return f'入力値: {input_value or ""}'
```

OutputとInputの役割
Output: 「どこに結果を表示するか」を指定

Output('コンポーネントID', 'プロパティ名')
例：Output('text-output', 'children') → text-outputの中身を更新

Input: 「何をきっかけに実行するか」を指定

Input('コンポーネントID', 'プロパティ名')
例：Input('text-input', 'value') → テキスト入力の値が変わったら実行

コードを書く手順

レイアウトでIDを設定
pythondcc.Input(id='text-input')  # 入力元
html.Div(id='text-output')  # 出力先

コールバックで関係を定義
python@app.callback(
    Output('出力先ID', 'プロパティ'),
    Input('入力元ID', 'プロパティ')
)

関数で処理を実装
pythondef 関数名(入力値):
    return 出力したい値


覚え方: Input（きっかけ）→ 関数実行 → Output（結果表示）の流れ

## InputとState（Reactのstateとは別概念）

```python
@app.callback(
    Output('greeting', 'children'),
    Input('button', 'n_clicks'),        # onClick的なトリガー
    State('name-input', 'value')        # 現在値の参照のみ
)
def greet(n_clicks, name):
    if n_clicks and name:
        return f'Hello, {name}!'
    return ''
```

日本語での簡潔な説明

### 要点

- **Dashのコールバック** = 宣言的なイベント処理 + 状態更新
- **サーバーサイドで実行** = JSXのようにクライアントではない
- **1つのコールバックが複数コンポーネントに影響可能** = Reactより柔軟

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
