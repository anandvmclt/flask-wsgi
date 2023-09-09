from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def greet():
    return jsonify(message="Hello from Flask-Wsgi App!")

@app.route('/api/items')
def items():
    sample_items = [{"id": 1, "name": "item1"}, {"id": 2, "name": "item2"}]
    return jsonify(items=sample_items)

# if __name__ == "__main__":
#     app.run(debug=True)
