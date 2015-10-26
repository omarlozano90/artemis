__author__ = 'Macintosh'

import ply.lex as lex

#lexicon,
tokens = [ 'NAME',
           'NUMBER',
           'PLUS',
           'MINUS',
           'TIMES',
           'DIVIDE',
           'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_error (t):
    print('error')
    quit()

#no estoy seguro que hace
def t_NUMBER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t

#build the lexer
lex.lex()

