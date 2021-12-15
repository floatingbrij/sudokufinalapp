# importing the required modules.
from flask import Flask, render_template, request, session, jsonify
from flask_session import Session
#importing our sudoku logic which can create, validate, and solve sudoku boards.
import suduko as s

#Creating our flask app and configuring our server side session.
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#When the user first connects with the server, the request is processed here.
@app.get('/')
def sudoku():
    #if the server contains a previous session of the same user then the sudoku board saved in session will be loaded and sent back to the user, else a new board will be created and sent back to the user.
    if not session.get("sudokulist"):
        a = s.createboard(3)
        session["sudokulist"] = a
        session["diff"] = 3
    else:
        a = session["sudokulist"]
    #this method 
    return render_template('basefiles/base1.html', sudoku = a)

#When the user clicks on any button, the request is processed here.
@app.post('/')
def sudokupost():
    data = request.json
    #if the button clicked is validate button, it routes here and returns the result.
    if data["type"] == "check":
        a = s.checkboard(data["board"])
        print(data,a)
        return jsonify(a)
    #if the button clicked is reset button, it routes here and returns the original board in session.
    if data["type"] == "reset":
        return jsonify(session["sudokulist"])
    #if the button clicked is show solution button, it routes here and returns the solution.
    if data["type"] == "solve":
        usersolve = s.solve(data["board"])
        print("user: ",usersolve)
        if usersolve == False:
            print("session:",s.solve(session["sudokulist"]))
            return jsonify(s.solve(session["sudokulist"]))      
        return jsonify(usersolve)
    #if the button clicked is New Game button, it routes here and returns a new game board.
    if data["type"] == "newgame":
        a = s.createboard(session["diff"])
        session["sudokulist"] = a
        return jsonify(a)
    #if the button clicked is difficulty button, it routes here and sets the required difficulty and returns a new board.
    if data["type"] == "setdiff":
        session["diff"]= data["diff"]
        return jsonify(True)
    
if __name__ == '__main__':
    #running the Flask Server ->
    app.run(host='0.0.0.0')