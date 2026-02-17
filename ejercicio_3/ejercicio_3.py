import sys
import ply.lex as lex

"""Los comentarios de una linea los podemos hacer con una linea, pero lso de
 mas de una debemos recurri a uan función"""
# Estados?

tokens = (
    "ID",
    "ASSING",
    "NUMBER"
)

"""Cuando ocurre algo que nos cambia las reglas, podemos usar estados"""
states = (
    ('comment', 'exclusive'),
)

t_ID = r'[a-zA-Z][a-zA-Z0-9_]'
t_ASSING = r':='
def t_NUMBER(token):
    r'0|[1-9][0-9]*'
    token.value = int(token.value)
    return token

def t_NEWLINE(token):
    r'\n+'
    """ Si el salto de linea tiene sentido nos vamos a saltar el return"""
    token.lexer.lineno += token.value.count("\n")

"""Vamos a poner un sting con todos los caractares que vamos a ignorar """
t_ignore = ' \t'

"""Esta función nos sirve para aquellos caracteres que no hemos reconocido"""
def t_error(token):
    print(f"Ilegal caracter at {token.lineno}, {token.lexpos}")
    token.lexer.skip(1)

def t_ONE_LINE_COMMENT(token):
    r'\#.*'
    """ Si el salto de linea tiene sentido nos vamos a saltar el return"""
    print(f"One line comment at {token.lineno}, {token.lexpos}")

def t_MULTI_LINE_COMMENT(token):
    r'\/\*(.|\n)*\*\/'
    new_lines = token.lineno + token.value.count("\n")
    """ Si el salto de linea tiene sentido nos vamos a saltar el return"""
    print(f"Multi line comment at {token.lineno}, {token.lexpos}")
    token.lexer.lineno = new_lines

def t_MULTI_LINE_COMMENT_START(token):
    r'\/\*'
    #Acedemos al lexer cuando detectamos que estamos comenzando un comentario
    # multi line y cambiamos al estado comment
    token.lexer.begin('comment')

def t_comment_CONTENT(token):
    # Si lo ponemos si el más puede reconocer expresiones vacias
    r'[^*/]+'
    new_lines = token.lineno + token.value.count("\n")
    print(f"Multi line comment at {token.lineno}, {token.lexpos}")
    token.lexer.lineno = new_lines

t_comment_ignore = ''

def t_comment_error(token):
    token.lexer.skip(1)

def t_comment_MULTI_LINE_COMMENT_stop(token):
    r'\*\/'
    # Cuando detectamos que estamos terminando un comentario
    # multi line y cambiamos al estado initial
    # no hay que crear initial, viene creado por defecto
    token.lexer.begin('INITIAL')

lexer = lex.lex()
lexer.input(open(file=sys.argv[1]).read())

for token in lexer:
    print(token.type, token.value)