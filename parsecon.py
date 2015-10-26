__author__ = 'Macintosh'

import ply.yacc as yacc
import lexicon

#lista de tokens
tokens = lexicon.tokens

def p_assign(p):
    '''assign : NAME EQUALS expr'''
    p[0] = ('ASSIGN', p[1],p[3])

def p_expr_plus(p):
    '''expr : term PLUS term'''
    p[0] = ('+', p[1],p[3])

def p_term_mul(p):
    '''term : term TIMES factor'''
    p[0] = ('*', p[1],p[3])

def p_term_factor(p):
    '''term : factor'''
    p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER'''
    p[0] = ('NUM', p[1])



data = "x = 3 * 4 + 5 * 6"

#build the parser
yacc.yacc()

t = yacc.parse(data)

print (t)