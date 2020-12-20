import sys
from antlr4 import *

from compiler import ExpressionListener, DefinitionsTreeListener
from compiler.custom_exceptions import CompilerInternalError, SyntacticAnalysisError
from antlr_generated import VYPLexer, VYPParser
from compiler.antlr_error_handler import CustomErrorListener


def main(argv):
    if argv.__len__() < 2:
        print("No input program specified in cmd argument.")
        return CompilerInternalError.exitCode
    if argv.__len__() == 3:
        sys.stdout = open(argv[2], 'w')


    try:
        input_stream = FileStream(argv[1])
        lexer = VYPLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = VYPParser(stream)
        parser.addErrorListener(CustomErrorListener())
        tree = parser.program()
        definitionListener = DefinitionsTreeListener()
        walker = ParseTreeWalker()
    except Exception as e:
        sys.stderr.write(str(e))
        exit(SyntacticAnalysisError.exitCode)


    try:
        walker.walk(definitionListener, tree)

        listener = ExpressionListener(definitionListener.getFunctionTable(), definitionListener.getClassTable())
        walker.walk(listener, tree)
    except Exception as e:
        sys.stderr.write(str(e))
        if e.exitCode == 1:
            exit(99)
        exit(e.exitCode)


if __name__ == '__main__':
    main(sys.argv)
