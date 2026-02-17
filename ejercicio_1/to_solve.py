#Lo primero es importar ply
import ply.lex as lex
import sys

#2 Definir que token PALABRA y token NÚMERO
# Solo son tokens letras y números, no vamos a tener en cuenta saltos de línea etc

tokens = (
    "WORD",
    "NUMBER"
)

a = 0b11

t_VARIABLE = r'[a-zA-Z][a-zA-Z0-9]*'
t_NUMBER = r'([1-9][0-9]*)|0'

#toke = {type, value, line, column}
def t_NUMBER(token) -> None:
    r'([1-9][0-9]*)|0'
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

#3. Construir el lexer
lexer = lex.lex()

#4a Ejecutar el lexer con una variable string
# lexer.input("palabra varible_1 123 19")
lexer.input("palabra variable_1 123 19")
for token in lexer:
    print(token.type, token.value)

#4b utilizar un fichero en vez de una varible
file = open(file=sys.argv[1])
data = file.read()
file.close()

lexer.input(data)
for token in lexer:
    print(token.type, token.value)
