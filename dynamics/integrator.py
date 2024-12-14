from abc import ABC, abstractmethod
import numpy as np

class BaseIntegrator(ABC):
    def __init__(self, system, parameters):
        self.system = system
        self.parameters = parameters
        self.time_step = parameters["time_step"]
        self.max_steps = parameters["max_steps"]

    @abstractmethod
    def update_positions(self):
        pass

    @abstractmethod
    def update_velocities(self):
        pass

class VelocityVerletIntegrator(BaseIntegrator):
    def update_positions(self, accelerations):
        self.system.positions += self.system.velocities * self.time_step + 0.5 * accelerations * self.time_step ** 2

    def update_velocities(self, accelerations):
        self.system.velocities += 0.5 * (self.system.accelerations + accelerations) * self.time_step
        self.system.accelerations = accelerations