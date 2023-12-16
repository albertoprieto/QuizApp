from flask import Flask, render_template, request, jsonify
import json
app = Flask(__name__)

@app.route('/')
def index():
    with open('preguntas.json', 'r') as f:
        data = json.load(f)

    return render_template('index.html',questions=data['medicina_interna'])


if __name__ == '__main__':
    app.run(debug=True)
