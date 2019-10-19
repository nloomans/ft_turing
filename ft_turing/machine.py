from enum import Enum


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
        else:
            raise ValueError('action must be either "LEFT" or "RIGHT"')

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
        if not self.blank in self.alphabet:
            raise ValueError('blank character not found in alphabet')
        for char in self.alphabet:
            if len(char) != 1:
                raise ValueError(
                    'all characters in alphabet must be 1 codepoint long')

        self.states = set(json['states'])
        self.final_states = json['finals']
        for state in self.final_states:
            if not state in self.states:
                raise ValueError('final state is not a valid state')

        self.transitions = {}
        for from_state, transitions in json['transitions'].items():
            for transition in transitions:
                if not from_state in self.states:
                    raise ValueError(
                        'transaction source state `%s\' is not a valid state' %
                        state)
                if not transition['to_state'] in self.states:
                    raise ValueError(
                        'transaction to_state `%s\' is not a valid state' %
                        transition.to_state)
                if not transition['read'] in self.alphabet:
                    raise ValueError(
                        'transaction read char `%s\' is not found in alphabet'
                        % transition.read)
                if not transition['write'] in self.alphabet:
                    raise ValueError(
                        'transaction write char `%s\' is not found in alphabet'
                        % transition.read)
                read = transition['read']
                if (from_state, read) in self.transitions:
                    raise ValueError(
                        f'dublicate transition {(from_state, read)}')
                self.transitions[(from_state, read)] = Transition(transition)

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
