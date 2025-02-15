'''
    project: VYPlanguage compiler
    authros: Tomáš Kožár, xkozar02
'''

class LexicalAnalysisError(Exception):
    exitCode = 11

class SyntacticAnalysisError(Exception):
    exitCode = 12

class SemanticTypeIncompatibilityError(Exception):
    exitCode = 13

class SemanticGeneralError(Exception):
    exitCode = 14

class CodeGenerationError(Exception):
    exitCode = 15

class CompilerInternalError(Exception):
    exitCode = 19