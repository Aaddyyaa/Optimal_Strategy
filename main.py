import numpy as np
from theory.value_iteration import value_iteration, extract_policy
from visualization.plot_policy import plot_policy

distances = np.linspace(0, 10, 50)
uncertainties = np.linspace(0, 3, 50)

V = value_iteration(distances, uncertainties)
policy = extract_policy(V, distances, uncertainties)

plot_policy(policy, distances, uncertainties)
