from lexer_class import LexerClass
import ply.yacc as yacc

# Clase que encapsula el analizador sintáctico (parser) del ejercicio 3.
# Este parser implementa una gramática que respeta la precedencia de operadores:
# la multiplicación y división tienen mayor prioridad que la suma y la resta.
# Esto se consigue dividiendo las expresiones en niveles (expresion_a, expresion_b, term).
class ParserClass:
    # PLY necesita que la clase del parser tenga acceso a la lista de tokens definida
    # en el lexer. Esta variable debe llamarse exactamente 'tokens'.
    tokens = LexerClass.tokens
    # Definimos explícitamente el símbolo de inicio de la gramática.
    start = 'expresion_a'

    def __init__(self):
        # yacc.yacc() construye las tablas de análisis sintáctico a partir de las reglas
        # gramaticales definidas en esta clase (las funciones que empiezan por p_).
        # El parámetro module=self le indica a PLY que busque las producciones gramaticales
        # dentro de esta instancia de la clase.
        self.parser = yacc.yacc(module=self)
        # Creamos una instancia del lexer para que el parser pueda alimentarse de tokens.
        self.lexer = LexerClass().lexer

    def p_expresion_a(self, p):
        '''expresion_a : expresion_a PLUS expresion_b
                       | expresion_a MINUS expresion_b
                       | expresion_b
        '''
        # Nivel más bajo de precedencia: suma y resta.
        # expresion_a puede ser:
        #   - Una expresion_a + expresion_b (suma)
        #   - Una expresion_a - expresion_b (resta)
        #   - Una expresion_b sola (delega al siguiente nivel de precedencia)
        # Al ser recursiva por la izquierda (expresion_a aparece a la izquierda),
        # las operaciones se agrupan de izquierda a derecha: 1 + 2 + 3 = (1 + 2) + 3
        print('expresion_a')

    def p_expresion_b(self, p):
        '''expresion_b : expresion_b TIMES term
                       | expresion_b DIVIDE term
                       | term
        '''
        # Nivel más alto de precedencia: multiplicación y división.
        # expresion_b puede ser:
        #   - Una expresion_b * term (multiplicación)
        #   - Una expresion_b / term (división)
        #   - Un term solo (delega al nivel más básico)
        # Al estar en un nivel inferior de la gramática, estas operaciones se evalúan
        # antes que la suma y la resta, respetando así la precedencia matemática.
        print('expresion_b')

    def p_term(self, p):
        '''term : NUMBER
                | LPAREN expresion_a RPAREN
        '''
        # Nivel más básico: un número o una subexpresión entre paréntesis.
        # term puede ser:
        #   - Un NUMBER (valor terminal, un número entero)
        #   - Una expresion_a entre paréntesis, lo que permite cambiar la precedencia
        #     natural. Por ejemplo, (1 + 2) * 3 fuerza a que la suma se evalúe primero.
        p[0] = p[1] if len(p) < 3 else p[2]

    def p_error(self, p):
        # Función que se ejecuta cuando el parser encuentra un error sintáctico,
        # es decir, cuando la secuencia de tokens no coincide con ninguna regla
        # gramatical definida.
        if p:
            print(f'Syntax error at line {p.lineno}, token {p.type}: {p.value}')
        else:
            print('Syntax error at EOF')

    def test(self, data):
        # Función auxiliar para probar el parser. Recibe un texto de entrada
        # y lo analiza sintácticamente utilizando el lexer y el parser.
        self.parser.parse(data)

    def test_with_file(self, file_path):
        # Función auxiliar para probar el parser con un archivo de entrada.
        # Abre el archivo especificado, lee todo su contenido y se lo pasa
        # al parser para que lo analice.
        with open(file_path, 'r') as file:      # Abrir el archivo en modo lectura
            data = file.read()                  # Leer todo el contenido del archivo
            self.test(data)                     # Pasar el contenido al parser
