import matplotlib.pyplot as plt

def plot_policy(policy, distances, uncertainties):
    plt.imshow(policy.T,
               origin='lower',
               extent=[0,10,0,3],
               aspect='auto')
    plt.xlabel("Distance")
    plt.ylabel("Uncertainty")
    plt.title("Optimal Policy (0=Stop, 1=Continue)")
    plt.colorbar()
    plt.show()
