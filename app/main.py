
from logger_instance import get_group_logger
from datetime import datetime
from lexer import lexer
from sintactico import parser
from config import settings

#No olvidar actualizar variables de entorno
logger = get_group_logger(settings.NOMBRE_AVANCE, settings.NOMBRE_ESTUDIANTE, datetime.now())

if __name__ == "__main__":
    while True:
        try:
            s = input('clojure > ')
        except EOFError:
            break
        if not s: continue
        result = parser.parse(s)
        print(result)