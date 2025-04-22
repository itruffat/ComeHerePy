import ply.lex as lex

tokens = (
    'NUMBER', 'STRING', 'VAR',
    'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD',
    'LPAREN', 'RPAREN', 'NEXT',
    'NOTE', 'CALL', 'ASK', 'TELL', 'COME', 'FROM', 'SGN'
)

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIV     = r'//'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NOTE(t): r'NOTE'; return t
def t_CALL(t): r'CALL'; return t
def t_ASK(t): r'ASK'; return t
def t_TELL(t): r'TELL'; return t
def t_COME(t): r'COME'; return t
def t_FROM(t): r'FROM'; return t
def t_SGN(t): r'SGN'; return t
def t_MOD(t): r'MOD'; return t

def t_STRING(t):
    r"'[^']*'"
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NEXT(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()
