from ply import yacc as yacc
from lexer import tokens
from logger_instance import logger

#Main syntax rule
def p_codigo(p):
    '''codigo : expresionAritmetica
              | impresion
              | condiciones
              | estructuraDatos
              | funcion
              | estructuraControl'''

#Expresiones
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

#Funciones
def p_funcion(p):
    '''funcion : LPAREN DEFN ID LBRACK argumentos RBRACK codigo RPAREN'''

def p_argumentos(p):
    '''argumentos : ID
                  | ID argumentos'''
#Asignaciones

#Estructuras de control
def p_estructuraControl(p):
    '''estructuraControl : estructuraIf
                        | ControlWhile'''

def p_estructuraIf(p):
    '''estructuraIf : LPAREN IF condicion codigo RPAREN
                    | LPAREN IF condicion codigo codigo RPAREN'''
    
def p_ControlWhile(p):
    'ControlWhile :  LPAREN WHILE LPAREN condiciones RPAREN LPAREN codigo RPAREN RPAREN'



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


#Estructuras de datos    
def p_estructuraDatos(p):
    '''estructuraDatos : LPAREN conjunto RPAREN''' 

def p_conjunto(p):
    '''conjunto : HASHSET valores RBRACE
                | SET LBRACK valores RBRACK'''

##PENDING lista

#Valores
def p_valor(p):
    '''valor : INT
        | FLOAT
        | STRING
        | ID'''
    
def p_valores(p):
    '''valores : valor 
            | valor valores'''
    
    
# Error rule for syntax errors
def p_error(p):
    if p:
        logger.warning(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    else:
        logger.warning("Syntax error: unexpected end of input")
    # print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


#TODO  asignacion variable, asignacion estructura, asignacion aritmetica, asignacion booleana (condicional)
#TODO  declaracion de una estructura de datos (lista y conjunto) + los otros de clojure
#TODO  declaracion aritmetica con uno o mas operadores
#TODO  impresión con cero, uno o más argumentos