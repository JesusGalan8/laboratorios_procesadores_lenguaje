import sys
import ply.lex as lex
import ply.yacc as yacc

tokens = ('ID', 'NUMBER', 'EQUAL', 'SEMICOLON')
#Podriamos ponerlo como tokens normales y funcionaria igual

t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUAL = r'='
t_SEMICOLON = r';'

def t_NUMBER(t):
    r'0|[1-9][0-9]*'
    t.value = int(t.value)
    return t

t_ignore = ' \t'

def t_NEW_LINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'lexical error with {t.value} at {t.lineno}')
    t.lexer.skip(1)

lexer = lex.lex()


input_data = open(sys.argv[1], 'r').read()

'''start = 'programa'def p_empty(p):
'''

# Puedo tener una función con todas las reglas de producción o bien tener 
# una función para cada regla de producción
def p_programa(p):
    # Si queremos poner más de una regla de producción en una función, 
    # hay que poner una nueva línea. Es obligatorio que cada regla de 
    # producción tenga su propia línea.
    '''programa : sentencia 
                | sentencia programa'''

def p_sentencia(p):
    '''sentencia : ID EQUAL NUMBER SEMICOLON'''

def p_error(p):
    print(f'syntax error with {p}')

parser = yacc.yacc()
input_data = open(sys.argv[1], 'r').read()

parser.parse(input_data)
