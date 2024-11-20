class Tape:
    def __init__(self, input_string, blank_symbol="#"):
        self.tape = {}
        self.blank_symbol = blank_symbol
        self.head_position = 0

        
        for i, symbol in enumerate(input_string):
            self.tape[i] = symbol

    def read(self):
        return self.tape.get(self.head_position, self.blank_symbol)

    def write(self, symbol):
        self.tape[self.head_position] = symbol

    def move(self, direction):
        if direction == "R":
            self.head_position += 1
        elif direction == "L":
            self.head_position -= 1
        elif direction == "N":
            pass  # No movement
        else:
            raise ValueError(f"Invalid tape displacement direction: {direction}")

    def __str__(self):
        
        positions = self.tape.keys()
        if positions:
            min_position = min(positions)
            max_position = max(positions)
        else:
            min_position = 0
            max_position = 0

        
        tape_str = ''
        for i in range(min_position, max_position + 1):
            symbol = self.tape.get(i, self.blank_symbol)
            if i == self.head_position:
                tape_str += f'[{symbol}]'  
            else:
                tape_str += symbol
        return tape_str
    def get_left_of_head(self):
        positions = sorted(self.tape.keys())
        left_positions = [pos for pos in positions if pos < self.head_position]
        left_symbols = ''.join(self.tape.get(pos, self.blank_symbol) for pos in left_positions)
        return left_symbols

    def get_under_and_right_of_head(self):
        positions = sorted(self.tape.keys())
        right_positions = [pos for pos in positions if pos >= self.head_position]
        right_symbols = ''.join(self.tape.get(pos, self.blank_symbol) for pos in right_positions)
        return right_symbols