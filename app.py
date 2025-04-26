from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a simple Flask app running in Docker! by yash pahalwani"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
