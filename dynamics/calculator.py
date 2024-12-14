import numpy as np
from abc import ABC, abstractmethod

class BaseCalculator(ABC):
    def __init__(self, system):
        self.system = system

    @abstractmethod
    def compute_forces(self):
        pass

class LennardJonesCalculator(BaseCalculator):
    def __init__(self, system, epsilon=1.0, sigma=1.0, cutoff=2.5):
        super().__init__(system)
        self.epsilon = epsilon
        self.sigma = sigma
        self.cutoff = cutoff

    def compute_forces(self):
        positions = self.system.positions
        num_atoms = self.system.num_atoms
        forces = np.zeros_like(positions)

        for i in range(num_atoms):
            for j in range(i+1, num_atoms):
                r_ij = positions[j] - positions[i]
                r = np.linalg.norm(r_ij)

                if (r>self.cutoff or r==0):
                    continue

                #Calculate lj forces
                f_scalar = 24 * self.epsilon * ((2 * (self.sigma / r) ** 12) - (self.sigma / r) ** 6) / r ** 2
                f_vector = f_scalar * (r_ij/r)

                forces[i] += f_vector
                forces[j] -= f_vector

        return forces


