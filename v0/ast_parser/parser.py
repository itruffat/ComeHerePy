from v0.ast_parser.lexer import tokens
from v0.misc.string_aux import encode_string
from v0.ast_parser.Nodes import *
import ply.yacc as yacc



# Precedence for expressions
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV', 'MOD'),
    ('right', 'SGN'),
)

def p_program(p):
    '''program : statements'''
    p[0] = p[1]

def p_statements(p):
    '''statements : statements NEWLINE statement
                  | statement'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[3]]

def p_statement_numbered(p):
    '''statement : NUMBER statement_body
                '''
    p[0] = NumberedStatement(p[1], p[2])

def p_statement_simple(p):
    '''statement : statement_body
                 '''
    p[0] = SimpleStatement(p[1])

def p_statement_body(p):
    '''statement_body : comment
                      | call
                      | ask
                      | tell
                      | come_from'''
    p[0] = p[1]

def p_comment_single(p):
    '''comment : NOTE VAR
               | NOTE MISC
               | NOTE NUMBER
               | NOTE STRING'''
    p[0] = Comment([p[2]])

def p_comment_chain(p):
    '''comment : comment VAR
               | comment MISC
               | comment NUMBER
               | comment STRING'''
    p[1].parts.append(p[2])
    p[0] = p[1]

def p_call(p):
    '''call : CALL expression VAR'''
    p[0] = Call(p[2], p[3])

def p_ask(p):
    '''ask : ASK VAR'''
    p[0] = Ask(p[2])

def p_tell(p):
    '''tell : TELL expressions
            | TELL expressions NEXT'''
    p[0] = Tell(p[2])

def p_expressions_single(p):
    'expressions : expression'
    p[0] = [p[1]]

def p_expressions_multiple(p):
    'expressions : expressions expression'
    p[0] = p[1] + [p[2]]

def p_come_from(p):
    '''come_from : COME FROM expression'''
    p[0] = ComeFrom(p[3])

def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = BinaryOp(p[1], p[2], p[3])

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIV factor
            | term MOD factor'''
    p[0] = BinaryOp(p[1], p[2], p[3])

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor_sgn(p):
    '''factor : SGN factor'''
    p[0] = UnaryOp("SGN", p[2])

def p_factor_group(p):
    '''factor : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_factor_number(p):
    '''factor : NUMBER'''
    p[0] = Const(p[1])

def p_factor_string(p):
    '''factor : STRING'''
    p[0] = Const(encode_string(p[1]))

def p_factor_var(p):
    '''factor : VAR'''
    p[0] = Var(p[1])

def p_error(p):
    print(f"Syntax error at {p.value!r} (type: {p.type})") if p else print("Unexpected end of input")

parser = yacc.yacc()
