import sys
from ply.lex import lex, TOKEN

#1 Token integer + float

tokens = (
    'INT_VALUE',
    'FLOAT_VALUE'
)

#2 Token number

int_value_regex = r'(0|[1-9][0-9]*)'
float_value_regex = rf'({int_value_regex})?\.{int_value_regex}'

# Primero hay que poner lo más especificio y luego lo más general
# ya que sino detectará un decimal como entero
@TOKEN(float_value_regex)
def t_FLOAT_VALUE(token):
    token.value = float(token.value)
    return token

@TOKEN(int_value_regex)
def t_INT_VALUE(token):
    token.value = int(token.value)
    return token


# El caso en el que solo tengo una función de number 
# y no tengo token int o token float, por lo que no me es
# necesario cambiar el tipo
'''
@TOKEN(rf'{int_value_regex}|{float_value_regex}')
def t_NUMBER(token):
    if '.' in token.value:
        token.value = float(token.value)
    else:
        token.value = int(token.value)
    return token
'''
t_ignore = ' \t'

def t_error(token):
    print(f'Caracter ilegal {token.value[0]} en la linea {token.lineno}, posicion {token.lexpos}')
    token.lexer.skip(1)

def t_NEWLINE(token):
    r'\n+'
    token.lexer.lineno += token.value.count('\n')

lexer = lex()
fc = open(file=sys.argv[1]).read()
lexer.input(fc)

for token in lexer:
    print(f'{token.type}, {token.value}')