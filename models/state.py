class State:
    def __init__(self, distance, energy, uncertainty):
        self.distance = distance
        self.energy = energy
        self.uncertainty = uncertainty

    def is_terminal(self):
        return self.distance <= 0 or self.energy <= 0
