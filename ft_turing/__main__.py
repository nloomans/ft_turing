"""42 Turing VM

Usage:
  ft_turing <machine> <input>
  ft_turing (-h | --help)

Operands:
  <machine>  The path of a json file containg the machine description.
  <input>    The input that the given machine takes.

Options:
  -h --help  Print this help file

"""

from docopt import docopt
import json
from ft_turing.machine import Machine, MachineException
from ft_turing.vm import VM
from ft_turing.validate import validate


def main():
    arguments = docopt(__doc__)
    machine_file_name = arguments['<machine>']
    vm_input = arguments['<input>']

    machine_json = None
    try:
        with open(machine_file_name, 'r') as machine_file:
            machine_json = json.loads(machine_file.read())
    except Exception as e:
        print(f"Unable to read machine: {e}")
        exit(1)

    try:
        validate(machine_json, vm_input)
    except AssertionError as e:
        print(f"Validation failed: {e}")
        exit(1)

    machine = Machine(machine_json)
    print(machine)
    vm = VM(machine, vm_input, machine_json['initial'])
    print("\n==> starting execution...\n")
    while True:
        try:
            did_halt = vm.step()
        except MachineException as e:
            print(f"\n==> machine execution failed: {e}\n")
            exit(1)
        if did_halt:
            break
    print(
        f"\n==> machine halted in state {vm.current_state} with tape {vm.tape}\n"
    )


if __name__ == '__main__':
    main()
