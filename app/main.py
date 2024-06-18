
from logger_instance import get_group_logger
from datetime import datetime
from lexer import lexer
#Reemplazar por mi_nombre por tu nombre
logger = get_group_logger("lexico", "mi_nombre", datetime.now())

if __name__ == "__main__":
    #Antes y despues de ejecutar una funcion usar esta funcion para ejecutar los logs
    

    #Andres Porrs Algoritmo 1
    data = '''
    ; Numero es par o impar
(defn determinar-paridad [numero]
  (if (integer? numero)
    (if (zero? (mod numero 2))
      "es par"
      "es impar")
    (str numero " no es un número entero")))
    '''
    
    logger.warning("Algoritmo 1")
    logger.warning(f"INPUT : {data}")
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No más entrada
        logger.warning(tok)

        
