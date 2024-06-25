
from logger_instance import get_group_logger
from datetime import datetime
from lexer import lexer
#Reemplazar por mi_nombre por tu nombre
logger = get_group_logger("lexico", "Andres Porras", datetime.now())

if __name__ == "__main__":
    #Antes y despues de ejecutar una funcion usar esta funcion para ejecutar los logs
    

    #Andres Porrs Algoritmo 1
    data = '''
    
    (defn longitud-cadena [s]
        ;; Verifica que el argumento sea una cadena
        (if (string? s)
            ;; Calcula la longitud iterando sobre cada carácter
            (loop [contador 0
                cadena s]
                (if (empty? cadena)
                contador
            (recur (inc contador) (subs cadena 1))))
            ;; Genera una excepción si el argumento no es una cadena
        (throw (IllegalArgumentException. "El argumento debe ser una cadena"))))
    
=======
    ; Numero es par o impar
(defn determinar-paridad [numero]
  (if (integer? numero)
    (if (zero? (mod numero 2))
      "es par"
      "es impar")
    (str numero " no es un número entero")))
>>>>>>> 154a9a9039fc31faee0e62643b55cd359bc24027
    '''
    
    logger.warning("Algoritmo 1")
    logger.warning(f"INPUT : {data}")
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No más entrada
        logger.warning(tok)


