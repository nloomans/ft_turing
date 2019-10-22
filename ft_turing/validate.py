def validate(machine_json, vm_input):
    assert isinstance(machine_json, dict), "toplevel must be object"

    assert 'name' in machine_json, "name missing"
    assert isinstance(machine_json['name'], str), "name must be of type string"

    assert 'alphabet' in machine_json, "alphabet missing"
    assert isinstance(machine_json['alphabet'],
                      list), "alphabet must be of type array"
    for char in machine_json['alphabet']:
        assert isinstance(char, str), "alphabet must be an array of strings"
        assert len(
            char) == 1, "alphabet must be an array of single character strings"

    assert 'blank' in machine_json, "blank missing"
    assert isinstance(machine_json['blank'],
                      str), "blank must be of type string"
    assert machine_json['blank'] in machine_json[
        'alphabet'], "blank must be in alphabet"

    assert 'states' in machine_json, "states missing"
    assert isinstance(machine_json['states'],
                      list), "states must be of type array"
    for state in machine_json['states']:
        assert isinstance(state, str), "states must be an array of strings"

    assert 'initial' in machine_json, "initial missing"
    assert isinstance(machine_json['initial'],
                      str), "initial must be of type string"
    assert machine_json['initial'] in machine_json[
        'states'], "initial must be in states"

    assert 'finals' in machine_json, "finals missing"
    assert isinstance(machine_json['finals'],
                      list), "finals must be of type array"
    for final in machine_json['finals']:
        assert isinstance(final, str), "finals must be an array of strings"
        assert final in machine_json[
            'states'], "all finals must be a valid state"

    assert 'transitions' in machine_json, "transitions missing"
    assert isinstance(machine_json['transitions'],
                      dict), "transitions must be of type object"
    for key, transition_list in machine_json['transitions'].items():
        assert isinstance(transition_list,
                          list), "transitions children must be of type array"
        assert key in machine_json[
            'states'], "transition must be a valid state"
        previous_read_keys = set()
        for transition in transition_list:
            assert isinstance(transition,
                              dict), "transition must be of type object"

            assert 'read' in transition, "transition must have key read"
            assert isinstance(transition['read'],
                              str), "transition read must be of type string"
            assert transition['read'] in machine_json[
                'alphabet'], "transition read must be in alphabet"
            assert transition[
                'read'] not in previous_read_keys, "transition read must be unique within state"
            previous_read_keys.add(transition['read'])

            assert 'to_state' in transition, "transition must have key to_state"
            assert isinstance(
                transition['to_state'],
                str), "transition to_state must be of type string"
            assert transition['to_state'] in machine_json[
                'states'], "transition to_state must be in states"

            assert 'write' in transition, "transition must have key write"
            assert isinstance(transition['write'],
                              str), "transition write must be of type string"
            assert transition['write'] in machine_json[
                'alphabet'], "transition write must be in alphabet"

            assert 'action' in transition, "transition must have key action"
            assert isinstance(transition['action'],
                              str), "transition action must be of type string"
            assert transition['action'] in [
                'LEFT', 'RIGHT'
            ], "transition action must be either LEFT or RIGHT"

    for char in vm_input:
        assert char in machine_json['alphabet'], "all input character must be found in alphabet"
        assert char != machine_json['blank'], "input character may not be blank"
