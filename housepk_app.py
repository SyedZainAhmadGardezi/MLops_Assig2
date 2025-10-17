from flask import Flask

app = Flask(__name__)

@app.route('/dashboard')
def dashboard():
    return "Dashboard Page - added after merge"


if __name__ == '__main__':
    app.run(debug=True)
