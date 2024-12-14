from utils.input_reader import read_input_file
from system import System
from dynamics.dynamics import Dynamics

def main():
    parameters = read_input_file('input.txt')
    system = System(parameters)

    print("\nAtom types:\n", system.atom_types)
    print("\nMasses:\n", system.masses)

    dynamics = Dynamics(system, parameters)
    dynamics.run()

    print("\nFinal positions:\n", system.positions)
    print("\nFinal velocities:\n", system.velocities)
    print("\n")

if __name__ == "__main__":
    main()