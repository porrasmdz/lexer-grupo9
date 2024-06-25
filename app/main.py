
from logger_instance import get_group_logger
from datetime import datetime
from lexer import lexer
<<<<<<< HEAD
from config import settings

#No olvidar actualizar variables de entorno
logger = get_group_logger(settings.NOMBRE_AVANCE, settings.NOMBRE_ESTUDIANTE, datetime.now())
=======
from sintactico import parser


#Reemplazar por mi_nombre por tu nombre
logger = get_group_logger("lexico", "Andres Porras", datetime.now())
>>>>>>> b47c95d9f0c2be2272006333a9d1999f4d401da1

if __name__ == "__main__":
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
    #Antes y despues de ejecutar una funcion usar esta funcion para ejecutar los logs
    logger.warning("Algoritmo 1")
    logger.warning(f"INPUT : {data}")
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No más entrada
        logger.warning(tok)


while True:
   try:
       s = input('clojure > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)