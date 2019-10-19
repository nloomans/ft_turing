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
from ft_turing.machine import Machine

def main():
    arguments = docopt(__doc__)
    machine_file_name = arguments['<machine>']
    machine_input = arguments['<input>']

    machine_json = None
    try:
        with open(machine_file_name, 'r') as machine_file:
            machine_json = json.loads(machine_file.read())
    except Exception as e:
        print(f"Unable to read machine: {e}")
        exit(1)
    machine = None
    try:
        machine = Machine(machine_json)
    except ValueError as e:
        print(f"Unable to parse machine: {e}")
        exit(1)
    print(machine)

if __name__ == '__main__':
    main()
