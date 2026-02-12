def cost_continue(state, alpha=1.0, beta=0.5, gamma=5.0):
    risk = state.uncertainty
    return alpha * 1.0 + beta * 1.0 + gamma * risk

def cost_stop(state, stop_penalty=10.0):
    return stop_penalty
