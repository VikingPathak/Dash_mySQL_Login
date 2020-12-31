import dash
import dash_bootstrap_components as dbc
from app.config import DATABASE, SECRET_KEY
from flask_mysqldb import MySQL


# Dash App
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True, 
    meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}], 
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Setup the Flask Server since Dash uses Flask as a wrapper.
server = app.server

server.config['MYSQL_HOST']     =  DATABASE['HOST']
server.config['MYSQL_USER']     =  DATABASE['USER']
server.config['MYSQL_PASSWORD'] =  DATABASE['PASSWORD']
server.config['MYSQL_DB']       =  DATABASE['NAME']
server.config['MYSQL_PORT']     =  DATABASE['PORT']
mysql = MySQL(server)

# Additional Configurations
server.config.update(
    SECRET_KEY=SECRET_KEY,
)