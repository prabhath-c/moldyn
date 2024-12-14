import numpy as np

class Dynamics:
    def __init__(self, system, parameters):
        self.system = system
        self.parameters = parameters
        self.calculator = self.system.calculator
        self.integrator = self.system.integrator

    def run(self):
        print("\n")
        for step in range(self.integrator.max_steps):
            print(f"Step {step + 1}/{self.integrator.max_steps}")

            forces = self.calculator.compute_forces()
            accelerations = forces / self.system.masses[:, np.newaxis]

            self.integrator.update_positions(accelerations)
            self.integrator.update_velocities(accelerations)

            self.system.accelerations = accelerations