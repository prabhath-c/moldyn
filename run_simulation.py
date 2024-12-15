from utils.input_handler import read_input_file
from system import System
from dynamics.dynamics import Dynamics
from time import time

def main():
    start = time()
    parameters = read_input_file('input.txt')
    system = System(parameters)

    dynamics = Dynamics(system, parameters)
    dynamics.run()

    end = time()

    print(f"Simulation completed in {end - start} seconds.")

if __name__ == "__main__":
    main()