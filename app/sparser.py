from ply import yacc as yacc
from lexer import tokens
from logger_instance import logger
from custom_errors import SemanticError

#Main syntax rule
variables ={}
def p_codigo(p):
    '''codigo : expresionesAritmeticas
              | impresion
              | condiciones
              | estructuraDatos
              | funcion
              | estructuraControl
              | asignacion
              | expresionesAritmeticas codigo
              | impresion codigo
              | condiciones codigo
              | estructuraDatos codigo
              | funcion codigo
              | estructuraControl codigo
              | asignacion codigo'''

#Expresiones
def p_expresionesAritmeticas(p):
        '''expresionesAritmeticas : expresionAritmetica
                | LPAREN operador expresionesAritmeticas expresionAritmetica RPAREN
        '''

    
    
def p_expresionAritmetica(p):
    '''expresionAritmetica : LPAREN operador valor valor RPAREN'''
      # expresión aritmética
    if isinstance(p[3], str) and p[3] not in variables:
        raise SemanticError(f"Variable '{p[3]}' no definida")
        
    if isinstance(p[4], str) and p[4] not in variables:
        raise SemanticError(f"Variable '{p[4]}' no definida")
        
    if not isinstance(p[3], int) and p[3] not in variables:
        
        raise SemanticError(f"Esta operacion solo puede realizarse entre numeros")
        
    if not isinstance(p[4], int) and p[4] not in variables:
        raise SemanticError(f"Esta operacion solo puede realizarse entre numeros")
    
    
def p_operador(p):
    '''operador : TIMES
                | PLUS
                | DIVIDE
                | MINUS'''
            
def p_impresion(p):
    '''impresion : LPAREN PRINT valores RPAREN
        | LPAREN PRINTLN valores RPAREN
        | LPAREN PRINT RPAREN
        | LPAREN PRINTLN RPAREN'''
    if isinstance(p[3], str) and p[3] not in variables:
        raise SemanticError(f"Variable '{p[3]}' no definida")

        

#Funciones
def p_funcion(p):
    '''funcion : LPAREN DEFN ID LBRACK argumentos RBRACK codigo RPAREN
            | LPAREN DEFN ID LBRACK RBRACK codigo RPAREN'''

def p_argumentos(p):
    '''argumentos : ID
                  | ID argumentos'''

#Asignaciones
def p_asignacion(p):
    '''
    asignacion : LPAREN DEF ID valor RPAREN
                | LPAREN DEF ID STRING RPAREN
               | LPAREN DEF ID estructuraDatos RPAREN
               | LPAREN LET LPAREN asignaciones RPAREN RPAREN
                
    '''
    if len(p)==6:
        variables [p[3]] = p[4]
        
            
def p_asignaciones(p):
    '''
    asignaciones : ID valor
                      | ID valor asignaciones
    '''
    variables[p[1]]= p[2]
    
#Estructuras de control
def p_estructuraControl(p):
    '''estructuraControl : estructuraIf
                        | ControlWhile
                        | estructuraFor'''

def p_estructuraIf(p):
    '''estructuraIf : LPAREN IF condicion codigo RPAREN
                    | LPAREN IF condicion codigo codigo RPAREN'''
    
def p_ControlWhile(p):
    'ControlWhile :  LPAREN WHILE LPAREN condiciones RPAREN LPAREN codigo RPAREN RPAREN'

def p_estructuraFor(p):
    '''estructuraFor : LPAREN FOR argumentoFor codigo RPAREN'''

def p_argumentoFor(p):
    '''argumentoFor : secuencia 
                | secuencia argumentoFor'''

def p_secuencia(p):
    '''secuencia : LBRACK ID LPAREN RANGE INT INT RPAREN RBRACK'''

def p_condiciones(p):
    '''condiciones : condicion
                | condicion conector condiciones'''
                
def p_condicion(p):
    '''condicion : LPAREN operComp valor valor RPAREN'''
    if isinstance(p[3], str) and p[3] not in variables:
        raise SemanticError(f"Variable '{p[3]}' no definida")
    if isinstance(p[4], str) and p[4] not in variables:
        raise SemanticError(f"Variable '{p[4]}' no definida")
    if not isinstance(p[3], int) and p[3] not in variables:
        raise SemanticError(f"Esta operacion solo puede realizarse entre numeros")
    if not isinstance(p[4], int) and p[4] not in variables:
        raise SemanticError(f"Esta operacion solo puede realizarse entre numeros")
    
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
    '''estructuraDatos : conjunto 
                    |   listas''' 


def p_conjunto(p):
    '''conjunto : HASHSET valores RBRACE
                | SET LBRACK valores RBRACK'''

##PENDING lista
def p_listas(p):
    '''listas : LPAREN LIST valores RPAREN
            | COMILLA LPAREN valores RPAREN'''

#def p_contenidolistas(p):
#    '''contenidolistas : COMILLA valor
#            | COMILLA valor contenidolistas
#            | valores'''
#Valores
def p_valor(p):
    '''valor : INT
        | FLOAT
        | STRING
        | ID'''

    if not isinstance(p[1], str) and not isinstance(p[1], int) and not isinstance(p[1], float) and p[1] not in variables:
        # logger.warning()
        raise SemanticError(f"Variable '{p[1]}' no definida")
        # return
    p[0] = p[1]  
    
    
def p_valores(p):
    '''valores : valor 
            | valor valores'''
    
    
# Error rule for syntax errors
def p_error(p):
    if p:
        raise SyntaxError(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}' of type '{p.type}'")
    else:
        raise SyntaxError("Syntax error: unexpected end of input")
    
    # print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


#TODO  asignacion variable, asignacion estructura, asignacion aritmetica, asignacion booleana (condicional)
#TODO  impresión con cero, uno o más argumentos