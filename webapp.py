from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 0 = OFF, 1 = ON (for ac/heat)
ac, heat, Room1Temp, Room2Temp, Room3Temp, Room4Temp, outsideTemp = 0, 0, 0, 0, 0, 0, 0
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
@app.route("/userinput", methods = ['POST'])
def userInput():
    global li
    li[0] = request.form.get("desiredtemp", default = "")
    li[1] = request.form.get("room", default = "")
    return jsonify(li)
@app.route("/input", methods = ['GET'])
def input():
    global li
    return jsonify(li)

# LIVE UPDATING THE TEMPERATURES OF THE ROOMS
@app.route('/room1', methods=['GET', 'POST'])
def room1():
    global Room1Temp
    if request.method == 'POST':
        Room1Temp = request.json.get('room1temp')
        return str(Room1Temp)
    elif request.method == 'GET':
        return str(Room1Temp)

@app.route('/room2', methods = ['GET', 'POST'])
def room2():
    global Room2Temp
    if request.method == 'POST':
        Room2Temp = request.json.get('room2temp')
        return str(Room2Temp)
    elif request.method == 'GET':
        return str(Room2Temp)

@app.route('/room3', methods = ['GET', 'POST'])
def room3():
    global Room3Temp
    if request.method == 'POST':
        Room3Temp = request.json.get('room3temp')
        return str(Room3Temp)
    elif request.method == 'GET':
        return str(Room3Temp)

@app.route('/room4', methods = ['GET', 'POST'])
def room4():
    global Room4Temp
    if request.method == 'POST':
        Room4Temp = request.json.get('room4temp')
        return str(Room4Temp)
    elif request.method == 'GET':
        return str(Room4Temp)

@app.route('/outside', methods = ['GET', 'POST'])
def outside():
    global outsideTemp
    if request.method == 'POST':
        outsideTemp = request.json.get('outside')
        return str(outsideTemp)
    elif request.method == 'GET':
        return str(outsideTemp)