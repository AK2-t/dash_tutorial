# Dash チュートリアル

## Reactに対するDashの利点

- **簡単なセットアップ**: ReactのビルドツールやDependencyと比較して、Dashは最小限の設定で済みます
- **Pythonベース**: すでにPythonに精通している場合、JavaScript、HTML、CSSを学ぶ必要がありません
- **データサイエンスとの統合**: pandas、numpy、scikit-learn、plotlyとのシームレスな統合が可能です
- **高速なプロトタイピング**: インタラクティブなダッシュボードやデータ可視化を素早く作成できます
- **単一言語**: フロントエンドとバックエンドの両方をPythonで記述でき、開発ワークフローがシンプルになります

## Dashの欠点

- **コードの保守性**: アプリケーションの複雑さが増すにつれて管理が難しくなる場合があります
- **UIの複雑さに制限**: 高度にインタラクティブまたは複雑なUIアプリケーションには最適ではありません
- **パフォーマンス**: 複雑な操作では、ネイティブJavaScriptフレームワークより遅くなる場合があります
- **カスタマイズの制限**: 純粋なReactアプリケーションと比較して柔軟性が低くなります
- **中小規模のアプリケーションに最適**: 大規模な本番アプリケーションよりも、プロトタイピングや単純なアプリケーションに適しています

## Dashにおける状態管理

Dashは状態管理にコールバックベースのリアクティブプログラミングモデルを使用します：

- **コールバック関数**: ユーザー操作に応じてコンポーネントを更新するための中核メカニズム
- **Stateオブジェクト**: コールバックをトリガーせずにコンポーネントの値を取得します
- **dcc.Store**: アプリケーションの状態を管理するためのクライアントサイドストレージコンポーネント
- **コールバックコンテキスト**: どの入力がコールバックをトリガーしたかに関する情報にアクセスします
- **パターンマッチングコールバック**: 動的なコンポーネントの作成と更新を処理します
- **クライアントサイドコールバック**: パフォーマンス向上のためにブラウザでコールバックを実行します

例:
```python
@app.callback(
    Output('output-div', 'children'),
    Input('input-button', 'n_clicks'),
    State('input-field', 'value')
)
def update_output(n_clicks, input_value):
    if n_clicks is None:
        return ""
    return f"入力値: {input_value}"
```

## DashにおけるUIの記述

Dashは宣言的なアプローチでUIを記述します：

- **コンポーネントベース**: 定義済みのコンポーネントを使用してUIを構築します
- **レイアウト定義**: Pythonオブジェクトと辞書を使用してUI構造を定義します
- **HTMLコンポーネント**: 基本的なHTML要素は`dash_html_components`（現在は`dash.html`）から利用可能です
- **コアコンポーネント**: インタラクティブな要素は`dash_core_components`（現在は`dash.dcc`）から利用可能です
- **コンポーネントプロパティ**: Python辞書を使用して外観と動作を設定します
- **インラインスタイリング**: CSSはPython辞書として適用されます
- **外部スタイルシート**: より複雑なスタイリングのために外部CSSファイルにリンクします

例:
```python
import dash
from dash import html, dcc

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('ダッシュボードタイトル', style={'textAlign': 'center'}),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'データA'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'データB'},
            ],
            'layout': {
                'title': 'サンプルグラフ'
            }
        }
    )
])
```

## Dashのページ機能

Dashは`dash.page_registry`モジュールを通じてマルチページアプリケーションをサポートします：

- **ディレクトリベースのルーティング**: `pages`ディレクトリで定義されたページに自動ルーティングが設定されます
- **ページ登録**: パス、タイトル、説明などのメタデータでページを登録します
- **URLルーティング**: クライアントサイドルーティングのための`dcc.Location`と`page_container`
- **ページナビゲーション**: 適切なパスを持つ`dcc.Link`または`html.A`を使用してリンクを作成します
- **共有レイアウト**: すべてのページで共有される共通要素
- **URLパラメータ**: コールバックでURLクエリパラメータにアクセスして使用します

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

Dashには複数のコンポーネントライブラリが利用可能です：

- **dash-bootstrap-components**: レスポンシブレイアウト用のBootstrapコンポーネント
- **dash-mantine-components**: マテリアルデザインにインスパイアされたコンポーネント
- **dash-ag-grid**: フィルタリング、ソート、編集機能を備えた高度なデータテーブル
- **dash-daq**: デジタル分析と定量的コンポーネント
- **dash-leaflet**: インタラクティブな地図
- **dash-cytoscape**: ネットワークグラフ可視化
- **dash-table**: インタラクティブなデータテーブル（Dashコアに含まれています）
- **dash-extensions**: さまざまな追加ユーティリティとコンポーネント

dash-bootstrap-componentsの使用例:
```python
import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("ダッシュボードタイトル"), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("カード1"),
                dbc.CardBody("これはカード1の内容です")
            ])
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("カード2"),
                dbc.CardBody("これはカード2の内容です")
            ])
        ], width=6)
    ])
])
```

## データ分析ライブラリとの統合

Dashは、Pythonのデータサイエンスエコシステムとシームレスに統合されます：

- **NumPy**: 数値計算に使用し、結果を直接可視化します
- **Pandas**: データを変換・分析し、dash-tableやグラフで表示します
- **Plotly**: Plotly ExpressやPlotly Graph Objectsを使用してインタラクティブな可視化を作成します
- **Scikit-learn**: MLモデルを構築し、予測やモデルのパフォーマンスを可視化します
- **SciPy**: 科学計算処理を実行し、結果を表示します
- **Statsmodels**: インタラクティブなパラメータ調整による統計モデリングを行います

例:
```python
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px

# NumPyとPandasを使用したサンプルデータ生成
np.random.seed(42)
df = pd.DataFrame({
    'x': np.random.normal(0, 1, 1000),
    'y': np.random.normal(0, 1, 1000),
    'category': np.random.choice(['A', 'B', 'C'], 1000)
})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dashによるデータ分析'),
    html.Div([
        dcc.Dropdown(
            id='category-filter',
            options=[{'label': cat, 'value': cat} for cat in df['category'].unique()],
            value=None,
            placeholder='カテゴリを選択'
        ),
    ]),
    dcc.Graph(id='scatter-plot')
])

@app.callback(
    Output('scatter-plot', 'figure'),
    Input('category-filter', 'value')
)
def update_graph(selected_category):
    filtered_df = df if selected_category is None else df[df['category'] == selected_category]
    
    fig = px.scatter(
        filtered_df, x='x', y='y',
        color='category', 
        title=f'散布図 {("" if selected_category is None else f"カテゴリ {selected_category} の")}'
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
```

## AIに書かせる時のtips

duplicate callbackによるエラーがよく起こる。
私は以下のようなプロンプトを注意事項として与えることが多い。
