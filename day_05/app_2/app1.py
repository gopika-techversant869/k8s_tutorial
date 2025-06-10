import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def call_app1():
    try:
        # Access the first app by its container name and port
        response = requests.get('http://flask_app1_container:5000/')
        return f"Response from app1: {response.text}"
    except Exception as e:
        return f"Failed to connect to app1: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
