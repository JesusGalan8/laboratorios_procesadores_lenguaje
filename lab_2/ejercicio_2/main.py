import sys

from lexer_class import LexerClass
from parser_class import ParserClass

# Punto de entrada del programa. Permite ejecutar solo el lexer o el parser completo
# según el argumento que se pase por línea de comandos.
# Uso:
#   python main.py just-lexer input    → Solo ejecuta el lexer (muestra los tokens)
#   python main.py parser input        → Ejecuta el parser completo (análisis sintáctico)

# sys.argv[1] es el modo de ejecución (just-lexer o parser)
# sys.argv[2] es la ruta al archivo de entrada
file = sys.argv[2]

if sys.argv[1] == 'just-lexer':
    # Si el usuario quiere solo el lexer, creamos una instancia del lexer
    # y leemos el archivo para tokenizarlo
    lexer = LexerClass()
    with open(file, 'r') as f:
        data = f.read()
    lexer.test(data)                    # Mostrar los tokens por pantalla
else:
    # Si no, ejecutamos el parser completo (que internamente usa el lexer)
    parser = ParserClass()
    parser.test_with_file(file)         # Analizar sintácticamente el archivo