from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

@app.route('/api/test')
def test():
    return jsonify({"message": "My first API is working!"})

@app.route('/api/AEE')
def aee():
    #call QuantumAEEUnit.py here
    from QuantumAEEUnit import QuantumAEEUnit
    unit = QuantumAEEUnit()
    unit.run()
    return jsonify({"message": "AEE is working!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
