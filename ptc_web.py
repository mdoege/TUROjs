import chess as c
import pyturochamp as p

from flask import Flask, request
app = Flask(__name__, static_url_path = '')

@app.route("/ptcmove", methods = ['POST'])
def ptcmove():
	print(request.content_type)
	print(request.is_json)
	content = request.get_json()
	fen = content['fen']
	print(fen)
	d = c.Board(fen)
	t, r = p.getmove(d, silent = True)
	print(r)
	return r[0]


app.run(host = '0.0.0.0', port = 5000)

