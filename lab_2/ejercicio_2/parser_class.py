from lexer_class import LexerClass
import ply.yacc as yacc

# Clase que encapsula el analizador sintáctico (parser) del ejercicio.
# El parser se encarga de verificar que la secuencia de tokens generada por el lexer
# cumple con las reglas gramaticales definidas. Utiliza la librería PLY (Python Lex-Yacc),
# que implementa un parser LALR(1), el mismo tipo de parser que usa la herramienta Yacc de Unix.
class ParserClass:
    # PLY necesita que la clase del parser tenga acceso a la lista de tokens definida
    # en el lexer. Esta variable debe llamarse exactamente 'tokens'.
    tokens = LexerClass.tokens

    def __init__(self):
        # yacc.yacc() construye las tablas de análisis sintáctico a partir de las reglas
        # gramaticales definidas en esta clase (las funciones que empiezan por p_).
        # El parámetro module=self le indica a PLY que busque las producciones gramaticales
        # dentro de esta instancia de la clase, en lugar de buscarlas en el módulo global.
        self.parser = yacc.yacc(module=self)
        # Creamos una instancia del lexer para que el parser pueda alimentarse de tokens.
        self.lexer = LexerClass().lexer

    def p_lamda(self,p):
        '''lamda : '''
        # Producción lambda (vacía). Representa la cadena vacía en la gramática.
        # Se utiliza cuando una regla necesita poder derivar en "nada".
        # Por ejemplo, si el programa puede terminar sin más sentencias.

    def p_programa(self, p):
        '''
        programa : sentencia
                 | sentencia NEW_LINE programa
        '''
        # Regla principal de la gramática. Define la estructura general del programa.
        # Un programa puede ser:
        #   - Una única sentencia
        #   - Una sentencia seguida de saltos de línea y otro programa (recursión)
        # Esta recursión permite que el programa tenga múltiples sentencias separadas
        # por saltos de línea. Es una definición recursiva por la derecha.

    def p_sentencia(self, p):
        '''
        sentencia : INT_VALUE operand INT_VALUE
        '''
        # Regla que define una sentencia como una operación aritmética simple:
        # un número entero, seguido de un operador (+/-), seguido de otro número entero.
        # Por ejemplo: 3 + 4, 2 - 1, 544 + 1231

    def p_operand(self, p):
        '''
        operand : PLUS
                | MINUS
        '''
        # Regla que define los operadores aritméticos válidos.
        # En este ejercicio solo se reconocen la suma (+) y la resta (-).
        # El parser simplemente verifica que el token sea uno de estos dos operadores.
    
    def p_error(self,p):
        # Función que se ejecuta cuando el parser encuentra un error sintáctico,
        # es decir, cuando la secuencia de tokens no coincide con ninguna regla
        # gramatical definida. El parámetro p contiene información sobre el token
        # que causó el error (tipo, valor, línea, posición).
        pass

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
