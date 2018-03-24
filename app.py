from flask import Flask, render_template, json, request, jsonify
from db import *

db = Database()
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')
    
@app.route('/update', methods=['POST'])
def update():
    name, age = request.form['name'], request.form['age']
    db.insertUser(name, age)
    return "hihi"

@app.route('/getall', methods=['GET', 'POST'])
def getall():
    data = db.getName()
    res = []
    for name, age in data:
        res.append((name, 2018-age))
    return jsonify(res)


if __name__ == "__main__":
    app.run(port=8080)