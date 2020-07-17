from flask import Flask, render_template, redirect, request, jsonify, abort
import json
import os

app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static/data", "data.json")
data = json.load(open(json_url))

def auth(user_key=None): 
    if user_key == "SOME_KEY": 
        return True
    return False 

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.route('/api/v1/', methods=['POST'])
def api():
    inp = request.json
    user_key = inp['key']
    if auth(user_key): 
        return jsonify(data)
    return jsonify(error="Invalid key"), 406
    
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', data=list(data))

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/checklist')
def checklist():
    return render_template('test.html') 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80) # host='127.0.0.1', port=8000, debug=True)
