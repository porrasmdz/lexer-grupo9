from gui import ClojureApp

#No olvidar actualizar variables de entorno para el logger
if __name__ == "__main__":
    app = ClojureApp()
    app.mainloop()
    # while True:
    #     try:
    #         s = input('clojure > ')
            
    #         logger.warning(f"INPUT : {s}")
        
    #     except EOFError:
            
    #         logger.warning(f"EOFError")
    #         break
    #     if not s: continue
    #     result = parser.parse(s)
        
    #     logger.warning(f"{result}")

