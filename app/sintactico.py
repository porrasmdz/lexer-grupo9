import ply.yacc as yacc

def p_expresionAritmetica(p):
    '''expresionAritmetica: operadores valores'''
    
def p_operadores(p):
    '''operadores:  PLUS
                | MINUS
                | TIMES
                | DIVIDE'''

def p_impresion(p):
    '''impresion: LPAREN PRINT valores RPAREN
        |LPAREN PRINTLN valores RPAREN
        |LPAREN PRINT RPAREN
        |LPAREN PRINTLN RPAREN'''
    
def p_valores(p):
    'valores: valor valor'

def p_valor(p):
    '''valor: INT
        |FLOAT
        |STRING
        |ID'''
        

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('lp > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
