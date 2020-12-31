import dash_bootstrap_components as dbc
import dash_html_components as html


layout = html.Div([
    dbc.Row(
        children=[
            dbc.Container(
            dbc.Row([
                dbc.Col([
                    html.H1("Login Successful.")
                ], width=5),
            ], style={"padding":"200px"}, justify="center")
        ),]
    )
])