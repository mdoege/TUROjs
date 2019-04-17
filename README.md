## TUROjs—[PyTUROCHAMP](https://github.com/mdoege/PyTuroChamp) as a Python web app

Install [Flask](http://flask.pocoo.org/) and [python-chess](https://github.com/niklasf/python-chess):

    pypy3 -m pip install Flask --user
    pypy3 -m pip install python-chess --user

(Of course you can also use regular Python 3, but PyPy is much faster.)

Start the web app:

    pypy3 ptc_web.py

Open this URL in your web browser:

[http://localhost:5000/index.html](http://localhost:5000/index.html)

Start play by dragging a white piece. If you want to switch sides, press the Get Move button. If you click the button repeatedly, the computer will play itself.

Reload the page to start a new game.

You can also select different engines: Bare, Bernstein, Plankalkül, and SOMA. The selection can be changed during a game, so e.g. each move can be played by a different engine.

### Speech synthesis browser support

The [Web Speech API](https://en.wikipedia.org/wiki/HTML5_audio#Web_Speech_API) is used to announce computer moves. This works best in the desktop versions of Firefox and Safari (i.e., the TUROjs welcome message is read too), whereas in desktop Chrome move announcement works but the welcome message on page load is blocked.

In mobile browsers, there is no speech output when it is not directly triggered by user interaction (e.g. pressing a button) and therefore it gets blocked in TUROjs completely.

### Other packages used

* [chess.js](https://github.com/jhlywa/chess.js)
* [chessboardjs](https://github.com/oakmac/chessboardjs)
* [jQuery](https://github.com/jquery/jquery)
