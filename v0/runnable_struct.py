from collections import defaultdict

from v0.lexer import lexer
from v0.parser import NumberedStatement, SimpleStatement, ComeFrom, parser
from v0.linked_statements import LinkedStatement, evaluate_expression

def _link_statements(statements:list[NumberedStatement | SimpleStatement]):
    linkeds = []
    previous = None
    for statement in statements:
        linkeds.append(LinkedStatement(statement, previous))
        previous = statement
    for n in range(len(linkeds)-1):
        linkeds[n].set_next(linkeds[n+1])
    return linkeds

def _index_by_line(statements: list[LinkedStatement]):
    ordered_statements = {}
    for statement in statements:
        if statement.number in ordered_statements.keys():
            raise Exception("repeated number")
        else:
            ordered_statements[statement.number] = statement
    return ordered_statements

def _comefrom_list(statements: list[LinkedStatement], variables: dict[str, int]):
    comefroms = {}
    for statement in statements:
        if isinstance(statement.body, ComeFrom):
            comefroms[statement.number] = evaluate_expression(statement.body.expr, variables)
    return comefroms

def _variables_list(statements: list[LinkedStatement]):
    variables = {}
    for statement in statements:
        for v in LinkedStatement.extract_vars(statement.body):
            variables[v] = 0
    return dict(variables)

def _update_triggers_list(statements: list[LinkedStatement]):
    variables = defaultdict(list)
    for statement in statements:
        if isinstance(statement.body, ComeFrom):
            for v in LinkedStatement.extract_vars(statement.body):
                variables[v].append(statement.number)
    return dict(variables)


def source_into_runnable_struct(code:str):
    parse_result = parser.parse(code, lexer=lexer)
    linkeds = _link_statements(parse_result)

    start_pointer = linkeds[0].number if linkeds else 0
    end_pointer = linkeds[-1].number if linkeds else 0
    indexed_statements = _index_by_line(linkeds)
    variables = _variables_list(linkeds)
    comefroms =  _comefrom_list(linkeds, variables)
    update_triggers = _update_triggers_list(linkeds)

    return (start_pointer, end_pointer), indexed_statements, comefroms, variables, update_triggers