class State:
    def __init__(self, name, is_final=False):
        self.name = name
        self.is_final = is_final

    def __str__(self):
        return self.name
