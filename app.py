from flask import Flask
from handlers.routes import configure_routes
from flask import Flask, Blueprint, jsonify, make_response
from flasgger import Swagger

app = Flask(__name__)
# app.register_blueprint(app_views)

app.config['MONGO_URI'] = "mongodb+srv://alquivago:alquivago123@cluster0.hhicxbc.mongodb.net/alquivago?retryWrites=true&w=majority"

configure_routes(app)

Swagger(app)

if __name__ == "__main__":
    app.run(debug=True)
