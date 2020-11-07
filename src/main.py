import sys
from antlr4 import *
from antlr_generated.VYPLexer import VYPLexer
from antlr_generated.VYPParser import VYPParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VYPLexer(input_stream)
    allTokens = lexer.getAllTokens()
    # for token in allTokens:
    #     print(token.text)

    stream = CommonTokenStream(lexer)
    parser = VYPParser(stream)
    tree = parser.program()
if __name__ == '__main__':
    main(sys.argv)
