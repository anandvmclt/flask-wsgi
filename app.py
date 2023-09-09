from flask import Flask, jsonify
from api import auth
from api.auth import bp as api_bp
from web.home import bp as web_bp

app = Flask(__name__)


app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(web_bp, url_prefix='/')



if __name__ == "__main__":
    app.run(debug=True)
