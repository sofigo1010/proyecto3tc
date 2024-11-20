from tape import Tape

class TuringMachine:
    def __init__(self, states, alphabet, tape_alphabet, initial_state, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.tape_alphabet = tape_alphabet
        self.initial_state = initial_state
        self.final_states = final_states  # Changed from final_state
        self.transitions = transitions

    def get_transition(self, current_state, tape_symbol):
        return self.transitions.get((current_state, tape_symbol))

    def simulate(self, input_string):
        tape = Tape(input_string, blank_symbol='#')
        current_state = self.initial_state

        step = 0  # Contador de pasos
        while True:
            # Obtener la descripción instantánea en formato u q v
            u = tape.get_left_of_head()
            v = tape.get_under_and_right_of_head()
            print(f"Paso {step}: {u} {current_state} {v}")

            tape_symbol = tape.read()
            transition = self.get_transition(current_state, tape_symbol)

            if transition is None:
                if current_state in self.final_states:
                    print("Cadena aceptada.")
                    return True
                else:
                    print(f"Cadena rechazada: No hay transición desde el estado {current_state} con el símbolo {tape_symbol}")
                    return False

            final_state, tape_output, tape_displacement = transition
            tape.write(tape_output)
            tape.move(tape_displacement)
            current_state = final_state

            if current_state == 'q_accept':
                # Mostrar la descripción instantánea final
                u = tape.get_left_of_head()
                v = tape.get_under_and_right_of_head()
                print(f"Paso {step + 1}: {u} {current_state} {v}")
                print("Cadena aceptada.")
                return True
            if current_state == 'q_reject':
                # Mostrar la descripción instantánea final
                u = tape.get_left_of_head()
                v = tape.get_under_and_right_of_head()
                print(f"Paso {step + 1}: {u} {current_state} {v}")
                print("Cadena rechazada: Estado de rechazo alcanzado.")
                return False

            step += 1
    

