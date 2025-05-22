import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Register this page in the app
dash.register_page(
    __name__, 
    path='/data-visualization',
    name="データ可視化", 
    order=2
)

# Generate sample data
np.random.seed(42)

# Time series data
dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
time_series_df = pd.DataFrame({
    'date': dates,
    'value_a': np.cumsum(np.random.normal(0, 1, 100)),
    'value_b': np.cumsum(np.random.normal(0, 2, 100))
})

# Scatter data
scatter_df = pd.DataFrame({
    'x': np.random.normal(0, 1, 200),
    'y': np.random.normal(0, 1, 200),
    'size': np.random.uniform(5, 25, 200),
    'category': np.random.choice(['A', 'B', 'C', 'D'], 200)
})

# Bar chart data
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
bar_df = pd.DataFrame({
    'category': categories,
    'value': np.random.randint(10, 100, len(categories))
})

# 3D data
n_points = 500
theta = np.random.uniform(0, 2*np.pi, n_points)
phi = np.random.uniform(0, np.pi, n_points)
r = np.random.normal(5, 1, n_points)

x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

three_d_df = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z,
    'group': np.random.choice(['Group 1', 'Group 2', 'Group 3'], n_points)
})

# Define the layout for this page
layout = html.Div([
    html.Div([
        html.H2("Dashでのデータ可視化", className="card-title"),
        html.P("このページでは、DashとNumPyやPlotlyなどのデータ分析ライブラリとの連携方法を紹介します。"),
    ], className="card"),
    
    # Time Series Visualization
    html.Div([
        html.H2("時系列可視化", className="card-title"),
        html.P("この例では、PlotlyとDashを使用してインタラクティブな時系列チャートを作成する方法を紹介します。"),
        
        html.Div([
            html.Label("変数を選択："),
            dcc.Checklist(
                id='timeseries-checklist',
                options=[
                    {'label': ' 値 A', 'value': 'value_a'},
                    {'label': ' 値 B', 'value': 'value_b'}
                ],
                value=['value_a', 'value_b'],
                inline=True,
                style={'marginBottom': '10px'}
            ),
            
            html.Label("日付範囲："),
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date=time_series_df['date'].min(),
                end_date=time_series_df['date'].max(),
                style={'marginBottom': '20px'}
            ),
            
            dcc.Graph(id='time-series-chart')
        ])
    ], className="card"),
    
    # Scatter Plot with Filtering
    html.Div([
        html.H2("インタラクティブな散布図", className="card-title"),
        html.P("この例では、フィルタリング機能を持つ散布図を紹介します。"),
        
        html.Div([
            html.Label("カテゴリを選択："),
            dcc.Dropdown(
                id='scatter-category-filter',
                options=[{'label': cat, 'value': cat} for cat in scatter_df['category'].unique()],
                value=None,
                placeholder="すべてのカテゴリ",
                style={'marginBottom': '20px'}
            ),
            
            dcc.Graph(id='scatter-plot')
        ])
    ], className="card"),
    
    # 3D Visualization
    html.Div([
        html.H2("3D可視化", className="card-title"),
        html.P("この例では、Plotlyを使用してインタラクティブな3D可視化を作成する方法を紹介します。"),
        
        html.Div([
            html.Label("グループを選択："),
            dcc.Dropdown(
                id='3d-group-filter',
                options=[
                    {'label': 'すべてのグループ', 'value': 'all'},
                    *[{'label': group, 'value': group} for group in three_d_df['group'].unique()]
                ],
                value='all',
                style={'marginBottom': '20px'}
            ),
            
            dcc.Graph(id='3d-scatter')
        ])
    ], className="card"),
    
    # Bar Chart with Sorting
    html.Div([
        html.H2("ソート機能付き棒グラフ", className="card-title"),
        html.P("この例では、ソートオプション付きの棒グラフを紹介します。"),
        
        html.Div([
            html.Label("並び替え順："),
            dcc.RadioItems(
                id='bar-sort-order',
                options=[
                    {'label': ' アルファベット順', 'value': 'alphabetical'},
                    {'label': ' 値の昇順', 'value': 'ascending'},
                    {'label': ' 値の降順', 'value': 'descending'}
                ],
                value='alphabetical',
                inline=True,
                style={'marginBottom': '20px'}
            ),
            
            dcc.Graph(id='bar-chart')
        ])
    ], className="card")
])

# Callbacks for interactive visualizations
@callback(
    Output('time-series-chart', 'figure'),
    Input('timeseries-checklist', 'value'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_timeseries(selected_values, start_date, end_date):
    if not selected_values:
        return px.line(title="少なくとも1つの変数を選択してください")
    
    filtered_df = time_series_df[
        (time_series_df['date'] >= start_date) & 
        (time_series_df['date'] <= end_date)
    ].copy()
    
    fig = go.Figure()
    
    if 'value_a' in selected_values:
        fig.add_trace(go.Scatter(
            x=filtered_df['date'],
            y=filtered_df['value_a'],
            mode='lines',
            name='値 A'
        ))
    
    if 'value_b' in selected_values:
        fig.add_trace(go.Scatter(
            x=filtered_df['date'],
            y=filtered_df['value_b'],
            mode='lines',
            name='値 B'
        ))
    
    fig.update_layout(
        title='時系列データ',
        xaxis_title='日付',
        yaxis_title='値',
        legend_title='変数',
        hovermode='x unified'
    )
    
    return fig

@callback(
    Output('scatter-plot', 'figure'),
    Input('scatter-category-filter', 'value')
)
def update_scatter(selected_category):
    filtered_df = scatter_df if selected_category is None else scatter_df[scatter_df['category'] == selected_category]
    
    fig = px.scatter(
        filtered_df, 
        x='x', 
        y='y',
        size='size',
        color='category',
        title=f"散布図 {'' if selected_category is None else f'カテゴリ {selected_category} の'}",
        labels={'x': 'X値', 'y': 'Y値', 'size': 'サイズ', 'category': 'カテゴリ'}
    )
    
    fig.update_layout(
        transition_duration=500
    )
    
    return fig

@callback(
    Output('3d-scatter', 'figure'),
    Input('3d-group-filter', 'value')
)
def update_3d_scatter(selected_group):
    filtered_df = three_d_df if selected_group == 'all' else three_d_df[three_d_df['group'] == selected_group]
    
    fig = px.scatter_3d(
        filtered_df,
        x='x',
        y='y',
        z='z',
        color='group',
        title=f"3D散布図 {'' if selected_group == 'all' else f'{selected_group} の'}"
    )
    
    fig.update_layout(
        scene=dict(
            xaxis_title='X軸',
            yaxis_title='Y軸',
            zaxis_title='Z軸'
        )
    )
    
    return fig

@callback(
    Output('bar-chart', 'figure'),
    Input('bar-sort-order', 'value')
)
def update_bar_chart(sort_order):
    df_sorted = bar_df.copy()
    
    if sort_order == 'alphabetical':
        df_sorted = df_sorted.sort_values('category')
    elif sort_order == 'ascending':
        df_sorted = df_sorted.sort_values('value')
    elif sort_order == 'descending':
        df_sorted = df_sorted.sort_values('value', ascending=False)
    
    fig = px.bar(
        df_sorted,
        x='category',
        y='value',
        color='value',
        title='ソートオプション付き棒グラフ',
        labels={'category': 'カテゴリ', 'value': '値'}
    )
    
    fig.update_layout(
        transition_duration=500
    )
    
    return fig