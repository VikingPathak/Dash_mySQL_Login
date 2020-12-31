import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from app import app, mysql
from flask import session
import random
import urllib


############ FORM COMPONENTS ##################################################
email_input = dbc.FormGroup(
    [
        dbc.Label("Username", html_for="txt_username", width=4, style={"font-weight":"bold"}),
        dbc.Col(
            dbc.Input(
                type="text", id="txt_username", placeholder="Enter email"
            ),
            width=8,
        ),
    ],
    row=True,
)

password_input = dbc.FormGroup(
    [
        dbc.Label("Password", html_for="txt_password", width=4, style={"font-weight":"bold"}),
        dbc.Col(
            dbc.Input(
                type="password",
                id="txt_password",
                placeholder="Enter password",
            ),
            width=8,
        ),
    ],
    row=True,
)

############# MAIN LAYOUT #####################################################
layout = html.Div(children=[
    dcc.ConfirmDialog(
        id='confirm',
        message='Username and(or) password missing !',
    ),
    dbc.Container(
        dbc.Row([
            dbc.Col([
                html.Div(email_input), 
                html.Div(password_input), 
                dbc.Col(
                    dbc.Button(
                        "Login", id="btn_login", color="dark", size="sm", style={"padding": ".25rem 1.5rem"}
                    ), 
                    width={"offset": 5, "order": "last"}
                ),
            ], width=5),
        ], style={"padding":"200px"}, justify="center")
    ),
    dcc.Location(id='login_url', refresh=True),
])
###############################################################################

# Callback for checking login details.
@app.callback(
    Output("login_url", 'pathname'),
    [
        Input(component_id='btn_login', component_property='n_clicks'),
        State(component_id='txt_username', component_property='value'),
        State(component_id='txt_password', component_property='value'),
    ], 
    prevent_initial_call=True
)
def login(n_clicks, username, password):
    if all([n_clicks, username, password]):
        query = f"""
            SELECT Password
            FROM _user
            WHERE Username='{username}';
        """
        cur = mysql.connection.cursor()
        cur.execute(query)
        result = cur.fetchall()

        if password != result[0][0]:
            return '/'

        session.permanent = False
        session['username'] = username
        n = random.randint(0, 999)
        path_encoded = urllib.parse.quote(f"/success?id={n}")
        return path_encoded

# Callback to throw alert for blank email/password
@app.callback(
    Output('confirm', 'displayed'),
    [
        Input(component_id='btn_login', component_property='n_clicks'),
        State(component_id='txt_username', component_property='value'),
        State(component_id='txt_password', component_property='value'),
    ], 
    prevent_initial_call=True
)
def display_confirm(n_clicks, username, password):
    if n_clicks:
        if not all([username, password]):
            return True
    return False
