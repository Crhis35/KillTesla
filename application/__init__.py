"""Iniciar app"""
from flask import Flask

def create_app():
    app = Flask(__name__,instance_relative_config=False)

    with app.app_context():
        # Import main Blueprint
        from application import routes
        app.register_blueprint(routes.main_bp)

        # Dash 
        from application.dash_app.graph import Add_Dash
        app = Add_Dash(app)

        #from application.assets import 

        return app
