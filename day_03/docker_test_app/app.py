from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    file_path = '/app/data/file1.txt'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as f:
        f.write('Hello, Docker Volume!\n')
    return 'File written successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
