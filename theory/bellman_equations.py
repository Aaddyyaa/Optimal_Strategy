import numpy as np

def value_iteration(distances, uncertainties, stop_penalty=10):
    V = np.zeros((len(distances), len(uncertainties)))

    for _ in range(100):
        for i, d in enumerate(distances):
            for j, u in enumerate(uncertainties):

                cost_stop = stop_penalty
                cost_continue = 1 + 5*u

                V[i,j] = min(cost_stop, cost_continue)

    return V
