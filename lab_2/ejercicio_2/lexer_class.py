import ply.lex as lex

# Clase que encapsula el analizador léxico (lexer) del ejercicio.
# El lexer se encarga de leer el texto de entrada y convertirlo en una secuencia
# de tokens. Cada token es una unidad mínima con significado, como un número,
# un operador o un salto de línea.
class LexerClass:
    # Lista de tokens que el lexer es capaz de reconocer. PLY necesita que esta
    # variable se llame exactamente 'tokens' y esté definida como atributo de clase.
    # Cada nombre de esta tupla debe tener una regla asociada (ya sea una variable
    # t_NOMBRE o una función t_NOMBRE).
    tokens = ('INT_VALUE', 'PLUS', 'MINUS', 'NEW_LINE')

    def __init__(self):
        # lex.lex() construye el autómata del lexer a partir de las reglas definidas
        # en esta clase. El parámetro module=self le indica a PLY que busque las reglas
        # (las funciones y variables que empiezan por t_) dentro de esta instancia.
        self.lexer = lex.lex(module=self)

    # Reglas simples definidas como variables. Para tokens cuyo patrón es una expresión
    # regular sencilla y no requieren procesamiento adicional, basta con asignar la
    # regex a una variable con el nombre t_NOMBRE_DEL_TOKEN.
    t_PLUS = r'\+'      # El símbolo '+'. Se escapa con '\' porque '+' es un metacarácter en regex
    t_MINUS = r'-'      # El símbolo '-'. No necesita escape porque no es metacarácter

    def t_INT_VALUE(self, t):
        r'0|([1-9][0-9]*)'
        # Regla para reconocer números enteros. Se define como función en lugar de variable
        # porque necesitamos transformar el valor: el lexer lee texto (string), pero nosotros
        # queremos trabajar con el valor numérico (int).
        # La regex acepta: el 0 solo, o un dígito del 1-9 seguido de cero o más dígitos.
        # Esto evita que se acepten números con ceros a la izquierda como '007'.
        t.value = int(t.value)      # Convertir la cadena de texto a un número entero
        return t                    # Devolver el token para que pase al parser

    def t_NEW_LINE(self, t):
        r'\n+'
        # Regla para reconocer uno o más saltos de línea consecutivos.
        # Se usa '\n+' para que múltiples líneas vacías se agrupen en un solo token.
        new_lines = t.value.count('\n')             # Contar cuántos saltos de línea hay
        t.value = f'{new_lines} new lines'          # Guardar un texto descriptivo como valor
        t.lexer.lineno += new_lines - 1             # Actualizar el contador de líneas del lexer
        return t                                    # Devolver el token

    # Caracteres que el lexer debe ignorar (no generar token). En este caso,
    # se ignoran los tabuladores y los espacios en blanco.
    t_ignore = '\t '

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
