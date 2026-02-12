import numpy as np

def value_iteration(distances, uncertainties,
                    stop_penalty=10,
                    gamma_risk=5,
                    max_iter=200):

    import numpy as np

    # Initialize value function
    V = np.zeros((len(distances), len(uncertainties)))

    goal_reward = -50  # reward (negative cost) for reaching goal

    for _ in range(max_iter):
        V_new = np.copy(V)

        for i, d in enumerate(distances):
            for j, u in enumerate(uncertainties):

                # Terminal condition: reached goal
                if d <= 0:
                    V_new[i, j] = goal_reward
                    continue

                # Cost of stopping
                cost_stop = stop_penalty

                # Approximate next state
                next_i = max(i - 1, 0)  # distance decreases
                next_j = min(j + 1, len(uncertainties) - 1)  # uncertainty increases

                # Cost of continuing
                cost_continue = 1 + gamma_risk * u + V[next_i, next_j]

                # Bellman update
                V_new[i, j] = min(cost_stop, cost_continue)

        V = V_new

    return V


def extract_policy(V, distances, uncertainties,
                   stop_penalty=10,
                   gamma_risk=5):

    policy = np.zeros_like(V)

    for i, d in enumerate(distances):
        for j, u in enumerate(uncertainties):

            cost_stop = stop_penalty

            next_i = max(i-1, 0)
            next_j = min(j+1, len(uncertainties)-1)

            cost_continue = 1 + gamma_risk*u + V[next_i, next_j]

            if cost_stop < cost_continue:
                policy[i,j] = 0  # stop
            else:
                policy[i,j] = 1  # continue

    return policy
