from typing import Optional

from v0.ast_parser.nodes import (Statement, NumberedStatement, SimpleStatement, ComeFrom, BinaryOp, UnaryOp, Var)


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

