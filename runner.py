import os
import sys

from v0.runnable_struct import source_into_runnable_struct
from v0.linked_statements import LinkedStatement
from v0.evaluator import evaluate_expression, evaluate_statement

def run_line(line_number, lines:dict[int|str, LinkedStatement], comefroms, variables, update_triggers):
    line = lines[line_number]
    changed = evaluate_statement(line, variables)
    to_be_changed = update_triggers[changed] if changed in update_triggers.keys() else []
    new_value_found = False
    for to_change in to_be_changed:
        old_value = comefroms[to_change]
        new_value = evaluate_expression(lines[to_change].body.expr, variables)
        comefroms[to_change] = new_value
        if new_value not in lines.keys():
            raise Exception("Invalid label to jump from")
        new_value_found |= old_value != comefroms[to_change]

def move_pointer_forward(line_number, lines, comefroms, end_point):
    if line_number == end_point or not lines[line_number].following:
        return None
    next_number = lines[line_number].following.number
    jump_to = next_number
    found_one = False
    for key, values in comefroms.items():
        if line_number == values:
            jump_to = key
            if found_one:
                raise Exception("Multi Comefroms asking for a jump")
            found_one = True
    return jump_to

def run(source):
    points, lines, comefroms, variables, update_triggers = source_into_runnable_struct(source)
    pointer = points[0]
    while pointer is not None:
        run_line(pointer, lines, comefroms, variables, update_triggers)
        pointer = move_pointer_forward(pointer, lines, comefroms, points[1])

def get_file_path_from_args():
    if len(sys.argv) < 2:
        print("Usage: python runner.py <file_path>")
        sys.exit(1)

    file_path = os.path.abspath(os.path.expanduser(sys.argv[1]))

    if not os.path.isfile(file_path):
        print("Invalid file path")
        sys.exit(1)

    return file_path

if __name__ == "__main__":
    code_path = get_file_path_from_args()
    with open(code_path, "r") as code_file:
        code = code_file.read()
    run(code)


