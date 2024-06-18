
from logger_instance import get_group_logger
from ply.lex import lex
from datetime import datetime

#Reemplazar por mi_nombre por tu nombre
logger = get_group_logger("lexico", "mi_nombre", datetime.now())

if __name__ == "__main__":
    #Antes y despues de ejecutar una funcion usar esta funcion para ejecutar los logs
    logger.warning("Min nombre")
