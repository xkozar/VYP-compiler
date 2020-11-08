import sys
from antlr4 import *
from antlr_generated.VYPLexer import VYPLexer
from antlr_generated.VYPParser import VYPParser
import compiler
import symbol_table

def main(argv):
    input_stream = FileStream("test.vyp")
    lexer = VYPLexer(input_stream)
    allTokens = lexer.getAllTokens()
    # for token in allTokens:
    #     print(token.text)

    stream = CommonTokenStream(lexer)
    parser = VYPParser(stream)
    tree = parser.program()
    

if __name__ == '__main__':
    main(sys.argv)
