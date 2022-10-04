from flask import Flask, render_template,request
from flask_socketio import SocketIO , send , join_room , leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

LED_SID = None

@socketio.on('message')
def handle_message(data):
    
    send(data , broadcast=True)

@socketio.on('join')
def on_join(data):
    LED_SID  = request.sid

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    socketio.run(app)