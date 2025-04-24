class Node: pass
class Statement(Node): pass
class NumberedStatement(Statement):
    def __init__(self, number, body): self.number = number ; self.body = body
class SimpleStatement(Statement):
    def __init__(self, body): self.body = body
class Comment(Node):
    def __init__(self, parts): self.parts = parts
class Call(Node):
    def __init__(self, expr, var): self.expr = expr; self.var = var
class Ask(Node):
    def __init__(self, var): self.var = var
class Tell(Node):
    def __init__(self, exprs): self.exprs = exprs
class ComeFrom(Node):
    def __init__(self, expr): self.expr = expr
class BinaryOp(Node):
    def __init__(self, left, op, right): self.left = left; self.op = op; self.right = right
class UnaryOp(Node):
    def __init__(self, op, val): self.op = op; self.val = val
class Var(Node):
    def __init__(self, name): self.name = name
class Const(Node):
    def __init__(self, value): self.value = value