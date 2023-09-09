from flask import Blueprint, jsonify

bp = Blueprint('tasks', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def list_tasks():
    # Your task listing logic here
    return jsonify({"tasks": ["API Listed -OK from VASS", 257]})
