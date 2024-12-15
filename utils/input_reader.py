import os

def read_input_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file: {file_path} does not exist.")
    
    parameters = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip and not line.startswith("#"):
                param_values = line.split(" ")
                if param_values[0].strip() in ['num_atoms', 'time_step', 'max_steps', 'temperature']:
                    parameters[param_values[0].strip()] = float(param_values[1].strip()) if '.' in param_values[1] or 'e' in param_values[1].lower() else int(param_values[1].strip())
                elif param_values[0].strip() in ['masses', 'box_size']:
                    parameters[param_values[0].strip()] = [float(value.strip()) for value in param_values[1:]]
                elif param_values[0].strip() in ['potential']:
                    parameters[param_values[0].strip()] = [param_values[1].strip()] + [float(value.strip()) for value in param_values[2:]]
                elif param_values[0].strip() in ['integrator']:
                    parameters[param_values[0].strip()] = param_values[1].strip()
        print(parameters)
    return parameters