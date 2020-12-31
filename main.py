from flask import session
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app, server
from pages import login_layout, index_layout


# Primary App Layout
app.layout = html.Div([
    dcc.Location(id='url_app', refresh=False), 
    dbc.Container(
        html.Div(id='page-content', children=[]),
        fluid=True
    )
])

# Initial App Callbacks for routing
@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url_app', component_property='pathname')], 
    prevent_initial_call=True
)
def display_page(pathname):
    if not session.get('username'):
        return login_layout
    if pathname == '/':
        return login_layout
    return index_layout

# Run the Server
if __name__ == '__main__':
    server.run(host="127.0.0.1", debug=True)