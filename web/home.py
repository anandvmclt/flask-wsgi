
from flask import Blueprint, render_template, jsonify

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/about', methods=['GET'])
def about():
    # Your task listing logic here
    return render_template('home.html')



@bp.route('/', methods=['GET'])
def index_fun():
    # Your task listing logic here
    return jsonify({"Home": "Succesfully loaded home page"})

