from turing_machine import TuringMachine

def parse_turing_machine(config):
    
    states = config["q_states"]["q_list"]
    initial_state = config["q_states"]["initial"]
    final_states = config["q_states"]["final"]

    
    alphabet = config["alphabet"]
    tape_alphabet = config["tape_alphabet"]

    transitions = {}
    for transition in config["delta"]:
        params = transition["params"]
        transition_initial_state = params["initial_state"]  
        tape_input = params["tape_input"]
        output = transition["output"]

        final_state = output["final_state"]
        tape_output = output["tape_output"]
        tape_displacement = output["tape_displacement"]

        transitions[(transition_initial_state, tape_input)] = (final_state, tape_output, tape_displacement)

    
    return TuringMachine(states, alphabet, tape_alphabet, initial_state, final_states, transitions)

