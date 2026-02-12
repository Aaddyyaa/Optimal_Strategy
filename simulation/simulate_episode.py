from models.dynamics import step

def simulate(policy, initial_state, max_steps=50):
    state = initial_state
    total_cost = 0

    for _ in range(max_steps):
        action = policy(state)

        if action == "stop":
            total_cost += 10
            break

        total_cost += 1 + 5 * state.uncertainty
        state = step(state)

        if state.is_terminal():
            break

    return total_cost
