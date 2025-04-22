from v0.runnable_struct import source_into_runnable_struct
from v0.linked_statements import evaluate_expression, evaluate_statement, LinkedStatement


def run_line(line_number, lines:  list[LinkedStatement], comefroms, variables, update_triggers):
    line = lines[line_number]
    changed = evaluate_statement(line, variables)
    to_be_changed = update_triggers[changed] if changed in update_triggers.keys() else []
    new_value_found = False
    for to_change in to_be_changed:
        old_value = comefroms[to_change]
        comefroms[to_change] = evaluate_expression(lines[to_change])
        new_value_found |= old_value != comefroms[to_change]

def move_pointer_forward(line_number, lines, comefroms, end_point):
    if line_number == end_point or not lines[line_number].following:
        return None
    next_number = lines[line_number].following.number
    jump_to = next_number
    for key, values in comefroms.items():
        if next_number in values:
            jump_to = key
    return jump_to

code = """ NOTE pass
10 CALL 'msg' pepe
CALL pepe-1 pepe
12 TELL pepe"""

if __name__ == "__main__":
    points, lines, comefroms, variables, update_triggers = source_into_runnable_struct(code)
    pointer = points[0]
    while pointer is not None:
        run_line(pointer, lines, comefroms, variables, update_triggers)
        pointer = move_pointer_forward(pointer, lines, comefroms, points[1])




