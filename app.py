from flask import Flask, render_template
from flask_socketio import SocketIO, emit  # type: ignore

app = Flask(__name__)

socketio = SocketIO(app)


@app.route("/chat")
def chat():
    return render_template("index.html")


@socketio.on("messagem")
def handle_message(msg):
    emit("messagem", msg, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, debug=True)
