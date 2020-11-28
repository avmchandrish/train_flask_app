from flask import Flask, render_template
from flask import request
from flask import jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/trains/')
def trains():
	fr = request.args['fr']
	to = request.args['to']
	dt = request.args['dt']
	import irctc_v1
	t=irctc_v1.run_crawls(fr, to, dt)
	return jsonify(t)

