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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


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
            return render_template('speed.html', result=result)
    else:
        return render_template('speed.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
