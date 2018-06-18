from flask import Flask
from flask_cors import *
from Model import db

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    db.init_app(app)

    # 解決跨域
    CORS(app, supports_credentials=True)

    return app


if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=True, host='0.0.0.0', port=6969)