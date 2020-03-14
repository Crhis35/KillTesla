"""Crear a Dash app"""
from pathlib import Path
import dash
import dash_html_components as html
import dash_core_components as dcc
from .layout import html_layout
from pymongo import MongoClient

def Add_Dash(server):
    """Crear a Dash app"""

    MONGO_URI = 'mongodb://localhost'
    client = MongoClient(MONGO_URI)

    result = collection.find()
    obj = set()
    options = []
    for (file) in result:
        obj.add(file['year'])
        


    colors = {'background':'#111111','text':'#7FDBFF'}
    external_stylesheets = [
        '/static/dist/css/styles.css',
        'https://fonts.googleapis.com/css?family=Lato',
        'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
    ]
    external_scripts = [
        '/static/dist/js/includes/jquery.min.js',
        '/static/dist/js/main.js'
    ]
    dash_app = dash.Dash(
        server=server,
        external_stylesheets=external_stylesheets,
        external_scripts=external_scripts,
        routes_pathname_prefix='/dashapp/'
    )
    dash_app.index_string = html_layout

    dash_app.layout = html.Div(
        children=[
            html.H1('Hello Dash!',style={'textAlign':'center','color':colors['text']}),
            dcc.Graph(
                id='example',
                figure={
                    'data':[
                        {'x':[1,2,3],'y':[4,1,2],'type':'bar','name':'SF'},{'x':[1,2,3],'y':[2,4,5],'type':'bar','name':'NYC'}
                    ],
                    'layout':{
                        'plot_bgcolor':colors['background'],
                        'paper_bgcolor':colors['background'],
                        'font':{'color':colors['text']},
                        'title': 'BAR PLOTS'
                    }
                }
            )
        ], 
        style={'backgroundColor':colors['background']},
        id='dash-container'
    )

    return dash_app.server