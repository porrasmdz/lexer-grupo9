
from lexer import lexer
from sparser import parser
from logger_instance import logger

#No olvidar actualizar variables de entorno para el logger
if __name__ == "__main__":
    while True:
        try:
            s = input('clojure > ')
            
            logger.warning(f"INPUT : {s}")
        
        except EOFError:
            
            logger.warning(f"EOFError")
            break
        if not s: continue
        result = parser.parse(s)
        
        logger.warning(f"{result}")

