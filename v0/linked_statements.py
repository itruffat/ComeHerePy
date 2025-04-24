from abc import abstractmethod, ABC
from typing import Optional

from v0.string_aux import decode_string, encode_string
from v0.parser import (Statement, NumberedStatement, SimpleStatement, ComeFrom, Call, BinaryOp, UnaryOp, Var, parser, \
                       Const, Ask, Tell, Comment)


class LinkedStatement(Statement):

    def __init__(self, source: NumberedStatement| SimpleStatement,
                 previous: Optional[NumberedStatement| SimpleStatement],
                 with_faux_number: Optional[int] = None):

        if hasattr(source, "number"):
            self.number = source.number
        elif with_faux_number:
            self.number = f"Faux_{with_faux_number}"
        elif previous and hasattr(previous, "number"):
            self.number = previous.number + 1
        else:
            self.number = 0
        self.body = source.body
        self.following = None

    def set_next(self, following: Optional["LinkedStatement"]):
        self.following = following

    @classmethod
    def extract_vars(cls, source):
        match source:
            case ComeFrom(expr=expr):
                return cls._recursive_extract_vars(expr)
            case _:
                return cls._recursive_extract_vars(source)

    @classmethod
    def _recursive_extract_vars(cls, source):
        match source:
            case BinaryOp(left=left, right=right):
                return cls._recursive_extract_vars(left) + cls._recursive_extract_vars(right)
            case UnaryOp(val=val):
                return cls._recursive_extract_vars(val)
            case Var(name=name):
                return [name]
            case _:
                return []

def evaluate_expression(expr, vars_dict):
    match expr:
        case Const(value=value):
            return value

        case Var(name=name):
            if name in vars_dict:
                return vars_dict[name]
            raise ValueError(f"Undefined variable: {name}")

        case BinaryOp(left=left, op=op, right=right):
            left_val = evaluate_expression(left, vars_dict)
            right_val = evaluate_expression(right, vars_dict)
            match op:
                case '+':
                    return left_val + right_val
                case '-':
                    return left_val - right_val
                case '*':
                    return left_val * right_val
                case '/':
                    return left_val // right_val
                case 'MOD':
                    return left_val % right_val
                case _:
                    raise ValueError(f"Unknown binary operator: {op}")

        case UnaryOp(op=op, val=val):
            new_val = evaluate_expression(val, vars_dict)
            match op:
                case 'SGN':
                    return 0 if new_val == 0 else new_val // abs(new_val)
                case _:
                    raise ValueError(f"Unknown unary operator: {op}")

        case _:
            raise TypeError(f"Unsupported expression type: {type(expr)}")


class IONamespace(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

    @abstractmethod
    def comment(self, data):
        pass

class DefaultIONamespace(IONamespace):
    def read(self):
        return input()

    def write(self, data):
        print(data)

    def comment(self, data):
        pass

defaultIO = DefaultIONamespace()

def evaluate_statement(stmt: Statement, vars_dict: dict[str, list[int] | int | float], io:IONamespace = defaultIO):
    match stmt.body:
        case Ask(var=var_name):
            if var_name in vars_dict:
                vars_dict[var_name] = encode_string(io.read())
            else:
                raise ValueError(f"Variable '{var_name}' not found")
            return var_name

        case Tell(exprs=exprs):
            output = [decode_string(evaluate_expression(expr, vars_dict)) for expr in exprs]
            io.write(''.join(output))
            return None

        case Call(var=var_name, expr=expr):
            val = evaluate_expression(expr, vars_dict)
            vars_dict[var_name] = val
            return var_name

        case Comment():
            return None

        case ComeFrom():
            return None

        case _:
            raise TypeError(f"Cannot evaluate statement of type: {type(stmt.body)}")
