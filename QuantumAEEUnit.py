import random

class QuantumAEEUnit:
    def __init__(self, name, state, awaken_fn, action_fn, evolve_fn):
        self.name = name
        self.state = state  # Simulated quantum state (dict with amplitudes or probabilities)
        self.awaken_fn = awaken_fn
        self.action_fn = action_fn
        self.evolve_fn = evolve_fn
        self.active = True

    def simulate_measurement(self):
        """Simulate a quantum measurement (collapse based on probability)"""
        probs = self.state["probabilities"]
        outcome = random.choices(list(probs.keys()), weights=probs.values())[0]
        self.state["last_measurement"] = outcome
        return outcome

    def should_awaken(self):
        result = self.simulate_measurement()
        return self.awaken_fn(result, self.state)

    def act(self):
        self.action_fn(self.state)

    def evolve(self):
        self.evolve_fn(self.state)


class QuantumAEEEngine:
    def __init__(self):
        self.units = []

    def register(self, unit):
        self.units.append(unit)

    def run(self):
        cycle = 0
        while any(unit.active for unit in self.units):
            print(f"\n--- CYCLE {cycle} ---")
            for unit in self.units:
                if unit.active and unit.should_awaken():
                    unit.act()
                    unit.evolve()
                elif unit.active:
                    print(f"{unit.name} is sleeping.")
            cycle += 1


# === EXAMPLE UNIT: A Quantum Counter ===

def awaken_if_heads(measured, state):
    return measured == "heads"

def count_energy(state):
    print(f"{state['name']} acts! Energy: {state['energy']}")
    state["energy"] -= 1
    if state["energy"] <= 0:
        state["active"] = False
        print(f"{state['name']} is now inactive.")

def evolve_random_flip(state):
    # Simulate a quantum state change
    if random.random() < 0.3:
        # 30% chance to flip probability
        state["probabilities"]["heads"], state["probabilities"]["tails"] = (
            state["probabilities"]["tails"],
            state["probabilities"]["heads"],
        )
        print(f"{state['name']} evolved: flipped quantum bias.")

# Define a unit with quantum-style state
unit1 = QuantumAEEUnit(
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

# Run it
#engine = QuantumAEEEngine()
#engine.register(unit1)
#engine.run()
