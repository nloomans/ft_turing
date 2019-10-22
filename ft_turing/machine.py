from enum import Enum


class MachineException(Exception):
    pass


class Action(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"


class Transition:
    def __init__(self, json):
        self.to_state = json['to_state']
        self.write = json['write']
        if json['action'] == "LEFT":
            self.action = Action.LEFT
        elif json['action'] == "RIGHT":
            self.action = Action.RIGHT

    def __str__(self):
        return "(%s, %s, %s)" % (self.to_state, self.write, self.action)

    def __resp__(self):
        return "<%s to %s, moving %s, writing %s>" % (
            self.__class__.__name__, self.to_state, self.action, self.write)


class Machine:
    def __init__(self, json):
        self.name = json['name']

        self.alphabet = set(json['alphabet'])
        self.blank = json['blank']

        self.states = set(json['states'])
        self.final_states = json['finals']

        self.transitions = {}
        for from_state, transitions in json['transitions'].items():
            for transition in transitions:
                self.transitions[(from_state, transition['read'])] = Transition(transition)

    def run(self, from_state, read):
        if (from_state, read) in self.transitions:
            return self.transitions[(from_state, read)]
        else:
            raise MachineException(
                f"no transition for {read} from state {from_state}")

    def __str__(self):
        string = f"""name: {self.name}
alphabet: {self.alphabet}
    blank: {self.blank}
states: {self.states}
    finals: {self.final_states}
transitions:"""
        for (from_state, read), transition in self.transitions.items():
            string += f"\n    ({from_state}, {read}) -> {transition}"
        return string
