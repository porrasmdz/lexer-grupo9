from ply import yacc as yacc
from lexer import tokens

def p_codigo(p):
    '''codigo : expresionAritmetica
              | impresion
              | condiciones
              | listas'''

            
def p_ControlWhile(p):
    'ControlWhile :  LPAREN WHILE LPAREN condiciones RPAREN LPAREN codigo RPAREN RPAREN'
            
def p_expresionAritmetica(p):
    '''expresionAritmetica : LPAREN operadores valores RPAREN'''
    
def p_operadores(p):
    '''operadores :  PLUS
                | MINUS
                | TIMES
                | DIVIDE'''

def p_impresion(p):
    '''impresion : LPAREN PRINT valores RPAREN
        | LPAREN PRINTLN valores RPAREN
        | LPAREN PRINT RPAREN
        | LPAREN PRINTLN RPAREN'''
    

def p_valor(p):
    '''valor : INT
        | FLOAT
        | STRING
        | ID'''
    
def p_valores(p):
    'valores : valor valor'


def p_condiciones(p):
    '''condiciones : condicion
                | condicion conector condiciones'''
                
def p_condicion(p):
    '''condicion : LPAREN operComp valor valor RPAREN'''
    
def p_conector(p):
    '''conector : AND
                | OR'''
    
def p_operComp(p):
    '''operComp : EQUAL
            | NOT_EQUAL
            | GREATER_THAN
            | LESS_THAN
            | GREATER_EQUAL
            | LESS_EQUAL'''
    
def p_listas(p):
    '''listas : LPAREN elementos RPAREN'''

def p_elementos(p):
    '''elementos : valor
            | valor elementos'''
            
           
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
