#-------------------------------------
# ejercicio 4 -- Palabras reservadas
#-------------------------------------
import sys
import ply.lex as lex

#1 Definir palabras reservadas
reserved = (
    'VAR',
    'WHILE'
)

tokens = reserved + (
    #Id es el nombre de las variables
    'ID',
    'EQUALS',
    'INT_VALUE',
    'L_BRACKET',
    'R_BRACKET'

)

reserved_map = {

}
for r_type in reserved:
    # Esto solo incluye las palabras reservadas en minusculas
    reserved_map[r_type.lower()] = r_type
    # Esto solo incluye las palabras reservadas en mayusculas
    reserved_map[r_type.upper()] = r_type

print(reserved_map)

#2 Definirs tokens, incluyendo palabras reservadas

t_EQUALS = r'=='
t_L_BRACKET = r'\{'
t_R_BRACKET = r'\}'

# Para el int vamos a crear una función ya que puede tomar
# diferentes valores

def t_INT_VALUE(token):
    r'0[1-9][0-9]*'
    token.type = 'INT_VALUE'
    return token

def t_ID(token):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    # El tipo del token es tengo un diccionario y voy a hacer una llamada de get
    # que me devueleve el tipo
    token.type = reserved_map.get(token.value, 'ID')
    # El tipo va a pasar de ser ID a ser VAR si se encuentra en el diccionario
    # si no se encuentra en el diccionario, se queda como ID
    '''
    if token.value in reserved_map:
        token.type = reserved_map[token.value]
    '''
    return token

t_ignore = ' \t'

def t_NEW_LINE(token):
    r'\n+'
    token.lexer.lineno += token.value.count('\n')

def t_error(token):
    print(f"Error en la linea {token.lineno}, posicion {token.lexpos}")
    token.lexer.skip(1)

lexer = lex.lex()
file_content = open(file=sys.argv[1]).read()
lexer.input(file_content)

for token in lexer:
    print(f'{token.type}, {token.value},{token.lineno}')