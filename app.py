from flask import Flask, jsonify
from QuantumAEEUnit import QuantumAEEUnit, QuantumAEEEngine, awaken_if_heads, count_energy, evolve_random_flip
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Render!"

@app.route('/api/test')
def test():
    return jsonify({"message": "My ffirst API is working!"})

@app.route('/api/testaee')
def testaee():
    return jsonify({"message": "Test AEE is working!"})
 
#api to check if drkits.smartwayelectronics.in is live or not
@app.route('/api/check-website/<website>')
def check_website(website):
    try:
        response = requests.get('http://'+website)
        print(f"website resposne code",response.status_code)
        if response.status_code == 200:
            return jsonify({"message": "Website is live!"})
        else:
            return jsonify({"message": "Website is not live!"})
    except Exception as e:
        return jsonify({"message": "Error checking website!", "error": str(e)})
    


@app.route('/api/AEE')
def aee():         
    unit = QuantumAEEUnit(
        name="QCounter",
        state={
            "name": "QCounter",
            "energy": 3,
            "probabilities": {"heads": 0.6, "tails": 0.4},
            "last_measurement": None,
            "active": True,
        },
        awaken_fn=awaken_if_heads,
        action_fn=count_energy,
        evolve_fn=evolve_random_flip,
    )
    engine = QuantumAEEEngine()
    engine.register(unit)
    engine.run()
    return jsonify({"message": "AEE is working!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
