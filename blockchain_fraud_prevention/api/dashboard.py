from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Blockchain Fraud Prevention Dashboard"

if __name__ == '__main__':
    app.run(debug=True)
