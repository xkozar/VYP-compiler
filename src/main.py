import sys
from antlr4 import *

from compiler import ExpressionListener
from antlr_generated import VYPLexer, VYPParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VYPLexer(input_stream)

    stream = CommonTokenStream(lexer)
    parser = VYPParser(stream)
    tree = parser.program()
    listener = ExpressionListener()
    
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    # try:
    # except Exception as e:
    #     print(e)


if __name__ == '__main__':
    main(sys.argv)
