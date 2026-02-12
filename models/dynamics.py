import numpy as np

def step(state, velocity=1.0, energy_cost=1.0, noise_std=0.1):
    new_distance = state.distance - velocity + np.random.normal(0, noise_std)
    new_energy = state.energy - energy_cost
    new_uncertainty = state.uncertainty + abs(np.random.normal(0, noise_std))

    return type(state)(new_distance, new_energy, new_uncertainty)
