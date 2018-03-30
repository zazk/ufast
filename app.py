from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return "Go Sign UP"

if __name__ == "__main__":
    app.run()