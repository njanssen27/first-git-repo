from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save')
def save():
    os.system('python3 /home/pi/Desktop/spring2025_codes/midterm.py')  # Update with your script path
    return "Script executed successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


