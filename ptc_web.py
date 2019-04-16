import chess as c
import pyturochamp, bare, bernstein, plan, soma

from flask import Flask, request
app = Flask(__name__, static_url_path = '')

@app.route("/ptcmove", methods = ['POST'])
def ptcmove():
	content = request.get_json()
	fen = content['fen']
	engine = content['engine']
	print(fen)
	print(engine)
	d = c.Board(fen)
	if engine == "Bare":
		t, r = bare.getmove(d, silent = True)
	elif engine == "Bernstein":
		t, r = bernstein.getmove(d, silent = True)
	elif engine == "Plankalkül":
		t, r = plan.getmove(d, silent = True)
	elif engine == "SOMA":
		t, r = soma.getmove(d, silent = True)
	else:
		t, r = pyturochamp.getmove(d, silent = True)
	print(r[0])
	return r[0]

app.run(host = '0.0.0.0', port = 5000)

