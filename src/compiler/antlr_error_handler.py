'''
    project: VYPlanguage compiler
    authros: Tomáš Kožár, xkozar02
'''

from antlr4.error.ErrorListener import ErrorListener

from compiler.custom_exceptions import SyntacticAnalysisError

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntacticAnalysisError

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise SyntacticAnalysisError


    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise SyntacticAnalysisError

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise SyntacticAnalysisError
