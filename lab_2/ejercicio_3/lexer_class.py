import ply.lex as lex

# Clase que encapsula el analizador léxico (lexer) del ejercicio 3.
# Este lexer reconoce tokens para expresiones aritméticas con las 4 operaciones
# básicas (+, -, *, /) y paréntesis para agrupar subexpresiones.
class LexerClass:
    # Lista de tokens que el lexer es capaz de reconocer. Cada nombre debe tener
    # una regla asociada (variable t_NOMBRE o función t_NOMBRE).
    tokens = ('NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

    def __init__(self):
        # lex.lex() construye el autómata del lexer a partir de las reglas definidas
        # en esta clase. El parámetro module=self le indica a PLY que busque las reglas
        # dentro de esta instancia.
        self.lexer = lex.lex(module=self)

    # Reglas simples definidas como variables. Para tokens cuyo patrón es una expresión
    # regular sencilla y no requieren procesamiento adicional.
    t_PLUS = r'\+'          # El símbolo '+'. Se escapa porque '+' es metacarácter en regex
    t_MINUS = r'-'          # El símbolo '-'
    t_TIMES = r'\*'         # El símbolo '*'. Se escapa porque '*' es metacarácter en regex
    t_DIVIDE = r'/'         # El símbolo '/'
    t_LPAREN = r'\('        # Paréntesis izquierdo '('. Se escapa porque '(' es metacarácter
    t_RPAREN = r'\)'        # Paréntesis derecho ')'. Se escapa porque ')' es metacarácter

    def t_NUMBER(self, t):
        r'0|([1-9][0-9]*)'
        # Regla para reconocer números enteros. Se define como función porque necesitamos
        # transformar el valor de string a int.
        # La regex acepta: el 0 solo, o un dígito del 1-9 seguido de cero o más dígitos.
        t.value = int(t.value)      # Convertir la cadena de texto a un número entero
        return t                    # Devolver el token para que pase al parser

    def t_newline(self, t):
        r'\n+'
        # Regla para contar los saltos de línea y actualizar el contador de líneas
        # del lexer. No devuelve token porque los saltos de línea no son relevantes
        # para la gramática de este ejercicio.
        t.lexer.lineno += len(t.value)

    # Caracteres que el lexer debe ignorar (espacios y tabuladores)
    t_ignore = ' \t'

    def t_error(self, t):
        # Función que se ejecuta cuando el lexer encuentra un carácter que no
        # coincide con ninguna regla definida. Es el manejador de errores léxicos.
        print(f'Illegal character {t.value[0]}')    # Imprimir el carácter problemático
        t.lexer.skip(1)                             # Saltar ese carácter y seguir analizando

    def test(self, data):
        # Función auxiliar para probar el lexer de forma aislada.
        # Recibe un texto de entrada, lo tokeniza y muestra cada token por pantalla.
        self.lexer.input(data)                      # Alimentar el lexer con el texto de entrada
        for token in self.lexer:                    # Iterar sobre cada token generado
            print(f'Token: {token.type}, Value: {token.value}, Line: {token.lineno}, Position: {token.lexpos}')
