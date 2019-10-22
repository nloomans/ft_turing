from colorama import Fore, Style
from ft_turing.machine import Action, MachineException


class VMException(Exception):
    pass


class Tape:
    def __init__(self, blank, vm_input):
        self.blank = blank
        self.tape = {}
        self.index = 0
        for i, char in enumerate(vm_input):
            if char == blank:
                continue
            self.tape[i] = char

    def read(self):
        if self.index not in self.tape:
            return self.blank
        else:
            return self.tape[self.index]

    def write(self, char):
        if char == self.blank:
            if self.index in self.tape:
                del self.tape[self.index]
        else:
            self.tape[self.index] = char

    def move(self, action):
        if action == Action.LEFT:
            self.index -= 1
        elif action == Action.RIGHT:
            self.index += 1

    def __str__(self):
        str = ""
        indexes = sorted(self.tape)
        startIndex = min(indexes[0], self.index)
        endIndex = max(indexes[-1], self.index)
        str += f"[{startIndex}]"
        for index in range(startIndex, endIndex + 1):
            if self.index == index:
                str += Style.BRIGHT + Fore.RED
            if index not in self.tape:
                str += Style.DIM + self.blank
            else:
                str += self.tape[index]
            str += Style.RESET_ALL
        str += f"[{endIndex}]"
        return str


class VM:
    def __init__(self, machine, machine_input, initial_state):
        self.machine = machine
        self.tape = Tape(machine.blank, machine_input)
        self.current_state = initial_state

    def step(self):
        state_max_len = len(
            sorted(self.machine.states, key=lambda state: len(state))[-1])
        print(f" {self.current_state.rjust(state_max_len)} {self.tape} ",
              end='')

        try:
            transition = self.machine.run(self.current_state, self.tape.read())
            print(transition)
        except MachineException as e:
            print(f"{Style.DIM}{e}{Style.RESET_ALL}")
            raise e

        self.current_state = transition.to_state
        self.tape.write(transition.write)
        self.tape.move(transition.action)

        return self.current_state in self.machine.final_states
