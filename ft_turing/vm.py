from ft_turing.machine import Action


class VMException(Exception):
    pass


class Tape:
    def __init__(self, alphabet, blank, vm_input):
        self.alphabet = alphabet
        self.blank = blank
        self.tape = {}
        self.index = 0
        for i, char in enumerate(vm_input):
            if char not in self.alphabet:
                raise ValueError(
                    f"input character '{char}' was not found in alphabet")
            if char == blank:
                continue
            self.tape[i] = char

    def read(self):
        if self.index not in self.tape:
            return self.blank
        else:
            return self.tape[self.index]

    def write(self, char):
        if char not in self.alphabet:
            raise ValueError(
                f"input character '{char}' was not found in alphabet")
        if char == self.blank:
            if self.index in self.tape:
                del self.tape[self.index]
        self.tape[self.index] = char

    def move(self, action):
        if action == Action.LEFT:
            self.index -= 1
        if action == Action.RIGHT:
            self.index += 1


class VM:
    def __init__(self, machine, machine_input, initial_state):
        self.machine = machine
        self.tape = Tape(self.machine.alphabet, machine.blank, machine_input)
        if initial_state not in self.machine.states:
            raise ValueError(
                f"initial state '{initial_state}' not found in {self.machine.states}"
            )
        self.current_state = initial_state

    def step(self):
        transition = self.machine.run(self.current_state, self.tape.read())
        print(transition)
        self.current_state = transition.to_state
        self.tape.write(transition.write)
        self.tape.move(transition.action)

        return self.current_state in self.machine.final_states
