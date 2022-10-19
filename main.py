from flask import Flask, render_template,request
from flask_socketio import SocketIO , send , join_room , leave_room
from flask_restful import Resource , Api 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
api = Api(app)

Current_Colror : str = "#ffffff"

class Color(Resource):
    
    def get(self):
        return {"color" : Current_Colror}

api.add_resource(Color , '/api/color')


@app.route("/" , methods = ["POST" , "GET"])
def index():
    
    global Current_Colror
    
    if request.method == "POST":
        Current_Colror = request.form["color"]
        
        
    return render_template("index.html" , color = Current_Colror)

if __name__ == '__main__':
    app.run(debug=True)