from simulation.simulate_episode import simulate
import numpy as np

def evaluate_policy(policy, initial_state, runs=100):
    costs = []

    for _ in range(runs):
        cost = simulate(policy, initial_state)
        costs.append(cost)

    return np.mean(costs), np.std(costs)
