import yaml
from parser import parse_turing_machine

def main():
   
    options = {
        "1": "config.yaml",
        "2": "alteradora.yaml"
    }

    
    print("Seleccione un archivo de configuración:")
    for key, value in options.items():
        print(f"{key}: {value}")

    
    choice = input("Ingrese el número correspondiente a su elección: ").strip()

    
    if choice not in options:
        print("Opción inválida. Por favor, intente de nuevo.")
        return

    
    config_file = options[choice]

    
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {config_file}.")
        return
    except yaml.YAMLError as e:
        print(f"Error al leer el archivo YAML: {e}")
        return

    
    turing_machine = parse_turing_machine(config)

    for input_string in config.get('simulation_strings', []):
        print(f"Simulando cadena: {input_string}")
        turing_machine.simulate(input_string)
        print("\n")

if __name__ == "__main__":
    main()
