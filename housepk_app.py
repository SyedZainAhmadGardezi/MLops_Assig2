from flask import Flask

app = Flask(__name__)

@app.route('/login')
def login():
    return "Login Page - by Dev1"

if __name__ == '__main__':
    app.run(debug=True)
