import sys
from antlr4 import *
from VYPLexer import VYPLexer
from VYPParser import VYPParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VYPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VYPParser(stream)
    tree = parser.program()
 
if __name__ == '__main__':
    main(sys.argv)