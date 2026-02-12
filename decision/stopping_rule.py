def threshold_policy(state, threshold=1.5):
    if state.uncertainty > threshold:
        return "stop"
    return "continue"
