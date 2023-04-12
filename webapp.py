from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 0 = OFF, 1 = ON
ac = 0
heat = 0
li = [0] * 2

# WEBAPP RENDERING
@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

# AC BUTTON (POST/GET)
@app.route('/acbutton', methods = ['POST'])
def acButton():
    global ac 
    ac = (ac + 1) % 2
    return str(ac)
@app.route('/acOnOff', methods = ['GET'])
def acOnOff():
    global ac
    return str(ac)

# HEAT BUTTON (POST/GET)
@app.route('/heatbutton', methods = ['POST'])
def heatButton():
    global heat
    heat = (heat + 1) % 2
    return str(heat)
@app.route('/heatOnOff', methods = ['GET'])
def heatOnOff():
    global heat
    return str(heat)

# DESIRED ROOM AND TEMP
@app.route("/userinput", methods = ["POST"])
def userInput():
    global li
    li[0] = request.form.get("desiredtemp", default = "")
    li[1] = request.form.get("room", default = "")
    return jsonify(li)
@app.route("/input", methods = ['GET'])
def input():
    global li
    return jsonify(li)