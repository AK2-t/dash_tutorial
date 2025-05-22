import dash
from dash import html, dcc

# Register this page in the app
dash.register_page(__name__, path='/', name="ホーム", order=0)

# Define the layout for this page
layout = html.Div([
    html.Div([
        html.H2("Dashチュートリアルへようこそ", className="card-title"),
        html.P("このインタラクティブチュートリアルでは、以下の機能を持つマルチページDashアプリケーションの構築方法を紹介します："),
        html.Ul([
            html.Li("様々なUIコンポーネントとレイアウト"),
            html.Li("データ分析ライブラリとの連携"),
            html.Li("適切な状態管理"),
            html.Li("インタラクティブな可視化")
        ]),
        html.P("上のナビゲーションバーを使って、Dashの様々な機能を探索してください。"),
    ], className="card"),
    
    html.Div([
        html.H2("チュートリアルセクション", className="card-title"),
        html.Div([
            html.Div([
                html.H3("UIコンポーネント"),
                html.P("Dashで利用可能な様々なUIコンポーネントを探索し、それらの効果的な使い方を学びましょう。"),
                dcc.Link("UIコンポーネントへ", href="/components", className="section-link")
            ], className="section-card"),
            
            html.Div([
                html.H3("データ可視化"),
                html.P("DashとNumPyやPlotlyなどのデータ分析ライブラリを連携させる方法を学びましょう。"),
                dcc.Link("データ可視化へ", href="/data-visualization", className="section-link")
            ], className="section-card"),
            
            html.Div([
                html.H3("状態管理"),
                html.P("Dashでのコールバックとステートオブジェクトを使ってアプリケーションの状態を管理する方法を理解しましょう。"),
                dcc.Link("状態管理へ", href="/state-management", className="section-link")
            ], className="section-card"),
        ], style={'display': 'grid', 'gridTemplateColumns': 'repeat(auto-fill, minmax(300px, 1fr))', 'gap': '20px'})
    ], className="card")
], style={'maxWidth': '1200px', 'margin': '0 auto'})