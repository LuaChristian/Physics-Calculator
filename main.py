from flask import *
from Math import Math
app = Flask(__name__)


@app.route("/home", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        typeOfEquation = request.form['equation']
        print(typeOfEquation)
        return redirect(url_for(typeOfEquation))
    return render_template('main.html')


@app.route("/speed", methods=["POST", "GET"])
def speed():
    time = ""
    distance = ""
    speed = ""
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            time = request.form['time']
            distance = request.form['distance']
            speed = request.form['speed']
            if time != "" and distance != "":
                distance = float(distance)
                time = float(time)
                speed = Math.speed(Math, distance, time)
                result = "Speed = " + str(round(speed, 3))
                return render_template('speed.html', result=result)
            elif distance != "" and speed != "":
                distance = float(distance)
                speed = float(speed)
                time = Math.time_speed(Math, distance, speed)
                result = "Time = " + str(round(time, 3))
                return render_template('speed.html', result=result)
            elif time != "" and speed != "":
                speed = float(speed)
                time = float(time)
                distance = Math.distance_speed(Math, speed, time)
                result = "Distance = " + str(round(distance, 3))
                return render_template('speed.html', result=result)
            else:
                result = "Keep one variable empty"
                return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


@app.route("/acceleration", methods=["POST", "GET"])
def acceleration():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('acceleration.html', result=result)
    else:
        return render_template('acceleration.html')


@app.route("/centripetal", methods=["POST", "GET"])
def centripetal():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('centripetal.html', result=result)
    else:
        return render_template('centripetal.html')


@app.route("/distance", methods=["POST", "GET"])
def distance():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('distance.html', result=result)
    else:
        return render_template('distance.html')


@app.route("/force", methods=["POST", "GET"])
def force():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('force.html', result=result)
    else:
        return render_template('force.html')


@app.route("/impulse", methods=["POST", "GET"])
def impulse():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('impulse.html', result=result)
    else:
        return render_template('impulse.html')


@app.route("/kinetic", methods=["POST", "GET"])
def kinetic():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('kinetic.html', result=result)
    else:
        return render_template('kinetic.html')


@app.route("/massflow", methods=["POST", "GET"])
def massflow():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('massflow.html', result=result)
    else:
        return render_template('massflow.html')


@app.route("/momentum", methods=["POST", "GET"])
def momentum():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('momentum.html', result=result)
    else:
        return render_template('momentum.html')


@app.route("/motion", methods=["POST", "GET"])
def motion():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('motion.html', result=result)
    else:
        return render_template('motion.html')


@app.route("/power", methods=["POST", "GET"])
def power():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('power.html', result=result)
    else:
        return render_template('power.html')


@app.route("/torque", methods=["POST", "GET"])
def torque():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('torque.html', result=result)
    else:
        return render_template('torque.html')


@app.route("/velocity", methods=["POST", "GET"])
def velocity():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('velocity.html', result=result)
    else:
        return render_template('velocity.html')


@app.route("/weight", methods=["POST", "GET"])
def weight():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('weight.html', result=result)
    else:
        return render_template('weight.html')


@app.route("/work", methods=["POST", "GET"])
def work():
    if request.method == "POST":
        print(request.form)
        if request.form.get('Backbutton'):
            return redirect(url_for('home'))
        elif request.form.get('calculate'):
            result = ""
            time = float(request.form['time'])
            distance = float(request.form['distance'])
            speed = Math.speed(Math, distance, time)
            result = speed
            return render_template('work.html', result=result)
    else:
        return render_template('work.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
