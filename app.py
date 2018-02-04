from flask import Flask, render_template, url_for, redirect, flash
from led import Led

app = Flask(__name__)
app.secret_key = 'secret-key'

# configure your Raspberry Pi IP address
raspberry_ip = '192.168.1.1'

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led/<string:status>', methods=['GET'])
def led(status):
    led = Led(pin=17)
    if status == 'on':
        led.turn_on()
        flash('Led is on.')
        return redirect(url_for('index'))
    elif status == 'off':
        led.turn_off()
        flash('Led is off.')
        return redirect(url_for('index'))
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host=raspberry_ip, port=5000)
