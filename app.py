import dash
from dash import Dash, html, dcc

# Create the Dash application with multi-page support
app = Dash(__name__, use_pages=True)

# Define the app layout with navigation and page container
app.layout = html.Div([
    # Header with title
    html.Div([
        html.H1('Dash チュートリアル', className='app-header-title')
    ], className='app-header'),
    
    # Navigation bar
    html.Div([
        html.Div([
            dcc.Link(
                f"{page['name']}", 
                href=page["relative_path"],
                className='nav-link'
            )
        ], className='nav-item') 
        for page in dash.page_registry.values()
    ], className='app-navigation'),
    
    # Page content container
    html.Div([
        dash.page_container
    ], className='app-content')
], className='app-container')

# Add custom CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&display=swap');
            
            body {
                font-family: 'Noto Sans JP', sans-serif;
                margin: 0;
                background-color: #f8f9fa;
                color: #343a40;
            }
            .app-container {
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }
            .app-header {
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                padding: 1.5rem;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .app-header-title {
                margin: 0;
                font-weight: 700;
                letter-spacing: 1px;
            }
            .app-navigation {
                display: flex;
                justify-content: center;
                background-color: white;
                padding: 0.75rem;
                overflow-x: auto;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                position: sticky;
                top: 0;
                z-index: 1000;
            }
            .nav-item {
                padding: 0 1.5rem;
            }
            .nav-link {
                color: #495057;
                text-decoration: none;
                font-weight: 500;
                padding: 0.5rem 0;
                display: inline-block;
                position: relative;
                transition: color 0.3s ease;
            }
            .nav-link:hover {
                color: #6a11cb;
            }
            .nav-link::after {
                content: '';
                position: absolute;
                width: 0;
                height: 2px;
                bottom: 0;
                left: 0;
                background-color: #6a11cb;
                transition: width 0.3s ease;
            }
            .nav-link:hover::after {
                width: 100%;
            }
            .app-content {
                flex: 1;
                padding: 2rem;
                max-width: 1200px;
                margin: 0 auto;
                width: 100%;
                box-sizing: border-box;
            }
            .card {
                background: white;
                border-radius: 12px;
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05), 0 4px 6px -2px rgba(0,0,0,0.03);
                padding: 1.5rem;
                margin-bottom: 2rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 20px -3px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05);
            }
            .card-title {
                margin-top: 0;
                color: #6a11cb;
                border-bottom: 1px solid #e9ecef;
                padding-bottom: 0.75rem;
                font-weight: 600;
                letter-spacing: 0.5px;
            }
            .section-card {
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.05);
                padding: 1.25rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .section-card:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 15px rgba(0,0,0,0.1);
            }
            .section-link {
                display: inline-block;
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                padding: 0.5rem 1rem;
                border-radius: 4px;
                text-decoration: none;
                font-weight: 500;
                margin-top: 1rem;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }
            .section-link:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)