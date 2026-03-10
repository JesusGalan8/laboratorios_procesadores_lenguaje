import ply.lex as lex
import sys
import ply.yacc as yacc

tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'SEMICOLON', 'L_PAREN', 'R_PAREN')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SEMICOLON = r';'
t_L_PAREN = r'\('
t_R_PAREN = r'\)'

def t_NUMBER(t):
    r'0|([1-9][0-9]*)'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f'Illegal character {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'UMINUS')
)

with open(sys.argv[1], 'r') as f:
    lexer.input(f.read())

for token in lexer:
    print(token)

# program : expresion : program | expresion ;
# expresion : expresion + expresion | expresion - expresion | expresion * expresion | expresion / expresion |
# ( expresion ) | NUMBER

def p_program(p):
    '''program : sentence SEMICOLON program
               | '''


def p_sentence(p):
    '''sentence : expresion SEMICOLON'''
    print(f'sentence: {p[1]}')

def p_expresion_binary(p):
    '''expresion : expresion PLUS expresion
                | expresion MINUS expresion
                | expresion TIMES expresion
                | expresion DIVIDE expresion'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expresion_unary(p):
    '''expresion : MINUS expresion %prec UMINUS'''
    p[0] = -p[2]

def p_expresion_paranthesis(p):
    '''expresion : L_PAREN expresion R_PAREN'''

def p_expresion_value(p):
    '''expresion : NUMBER'''
    p[0] = p[1]

def p_error(p):
    print(f'error with {p}')

parser = yacc.yacc()
with open(sys.argv[1], 'r') as f:
    file_content = f.read()
parser.parse(file_content)