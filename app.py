from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

@app.route('/api/test')
def test():
    return jsonify({"message": "API is working!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
