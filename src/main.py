import sys
from antlr4 import *
from antlr_generated.VYPLexer import VYPLexer
from antlr_generated.VYPParser import VYPParser
from antlr_generated.VYPListener import VYPListener
from compiler import *
from symbol_table import *

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VYPLexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = VYPParser(stream)
    tree = parser.program()
    listener = ExpressionListener()
    
    walker = ParseTreeWalker()
    try:
        walker.walk(listener, tree)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main(sys.argv)
