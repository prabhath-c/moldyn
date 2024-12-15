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

    def compute_forces_slow(self):
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
    
    def compute_forces(self):
        positions = self.system.positions
        forces = np.zeros_like(positions)

        distances_vector = positions[:, np.newaxis, :] - positions[np.newaxis, :, :]
        distances_scalar = np.linalg.norm(distances_vector, axis=-1)

        # Make sure division later by 0 is handled
        masked_distances = np.where((distances_scalar < self.cutoff) & (distances_scalar > 0), distances_scalar, np.inf)
        
        forces_scalar = 24 * self.epsilon * ((2 * (self.sigma / masked_distances) ** 12) - (self.sigma / masked_distances) ** 6) / masked_distances ** 2

        # To make sure
        forces_scalar = np.where(forces_scalar != np.inf, forces_scalar, 0)

        distances_scalar_safe = np.where(distances_scalar != 0, distances_scalar, np.inf)
        forces_vector = distances_vector * (forces_scalar[..., np.newaxis]/distances_scalar_safe[..., np.newaxis])

        forces = np.sum(forces_vector, axis=1)

        return forces
    
    def compute_forces_upper(self):
        positions = self.system.positions
        forces = np.zeros_like(positions)

        distances_vector = positions[:, np.newaxis, :] - positions[np.newaxis, :, :]
        distances_scalar = np.linalg.norm(distances_vector, axis=-1)
        distances_scalar_safe = np.where(distances_scalar > 0, distances_scalar, np.inf)

        upper_distances = np.triu(distances_scalar_safe, k = 1)

        # Make sure division later by 0 is handled
        masked_distances = np.where((upper_distances < self.cutoff) & (upper_distances > 0), upper_distances, np.inf)
        
        forces_upper = 24 * self.epsilon * ((2 * (self.sigma / masked_distances) ** 12) - (self.sigma / masked_distances) ** 6) / masked_distances ** 2

        forces_all = forces_upper + (-1)*forces_upper.T

        # To make sure
        forces_scalar = np.where(forces_all != np.inf, forces_all, 0)
        forces_vector = distances_vector * (forces_scalar[..., np.newaxis]/distances_scalar_safe[..., np.newaxis])

        forces = np.sum(forces_vector, axis=1)

        return forces