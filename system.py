import numpy as np
from dynamics.calculator import LennardJonesCalculator
from dynamics.integrator import VelocityVerletIntegrator

class System:
    def __init__(self, parameters):
        self.parameters = parameters
        self.num_atoms = parameters["num_atoms"]
        self.box_size = parameters["box_size"]
        self.masses_list = parameters["masses"]
        self.temperature = parameters["temperature"]
        self.potential = parameters["potential"][0]
        self.integrator = parameters["integrator"]

        self.positions = np.zeros((self.num_atoms, 3))
        self.velocities = np.zeros_like(self.positions)
        self.accelerations = np.zeros_like(self.positions)
        self.atom_types = np.zeros(self.num_atoms)

        self.__initialize_positions()
        self.__initialize_atom_types()
        self.__initialize_velocities()
        self.calculator = self.__select_calculator()
        self.integrator = self.__select_integrator()

    def __initialize_positions(self):
        self.positions = np.random.uniform(0, self.box_size, (self.num_atoms, 3))

    def __initialize_atom_types(self):
        self.atom_types = np.random.choice(len(self.masses_list), self.num_atoms)
        self.masses = np.array([self.masses_list[type] for type in self.atom_types])

    def __initialize_velocities(self):
        self.velocities = np.zeros((self.num_atoms, 3))
        for i, atom_type in enumerate(self.atom_types):
            mass = self.masses_list[atom_type]
            self.velocities[i] = np.random.normal(0, np.sqrt(self.temperature/mass), 3)
        
    def __select_calculator(self):
        if self.potential == 'lj':
            return LennardJonesCalculator(self,
                                          epsilon=self.parameters["potential"][1],
                                          sigma=self.parameters["potential"][2],
                                          cutoff=self.parameters["potential"][3])
        else:
            raise ValueError(f"Unsupported potential")
        
    def __select_integrator(self):
        if self.integrator == 'velocity_verlet':
            return VelocityVerletIntegrator(self, self.parameters)
        else:
            raise ValueError(f"Unsupported integrator")