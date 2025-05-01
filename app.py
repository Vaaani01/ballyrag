from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET'])
def submit():
    name = request.args.get('name')
    rollno = request.args.get('rollno')
    with open('logs.txt', 'a') as f:
        f.write(f'{datetime.datetime.now()} - Name: {name}, Roll No: {rollno}\n')
    return render_template('submit.html')

@app.route('/speedtest')
def speedtest():
    return render_template('speedtest.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
