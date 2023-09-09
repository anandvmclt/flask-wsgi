from flask import Flask, jsonify
from api import auth

app = Flask(__name__)


app.register_blueprint(auth.bp)



# if __name__ == "__main__":
#     app.run(debug=True)
