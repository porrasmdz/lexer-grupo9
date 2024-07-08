# lexer-grupo9

1. Actualizar el archivo .env (usar el contenido de example-env.dist)
2. Ejecutar los siguientes comandos
$pip install -r requirements.txt
$python -m venv venv
$.\venv\Scripts\activate (Para Windows)
$python ./app/main.py

#Parser codigo de casos de uso
##Impresión con cero, uno o más argumentos
(println)
(println "Hola, mundo!")
(println "El resultado es" (+ 2 3)) 

##Expresiones aritméticas con uno o más operadores
(+ 2 3)
(+ (* 2 3) (- 7 4)) !!TODO

##Condiciones con uno o más conectores
(if (< 5 10)  (println "5 es menor que 10") (println "5 no es menor que 10")) 
(if (< 5 10)  "5 es menor que 10" "5 no es menor que 10") !!TODO
(if (and (< 5 10) (not= 5 7)) "Ambas condiciones son verdaderas" "Al menos una condición no se cumple") !!TODO

##Definición de variables, todos los tipos, almacena resultados de expresiones/condicionales
(def x 10) 
(def y 3.14) !TODO
(def z true)
(def suma (+ 5 7)) !!TODO
(def es-mayor (if (> 15 10) true false)) !!TODO
(def lista-de-nombres '("Juan" "María" "Pedro")) !!TODO
(def conjunto-de-numeros #{1 2 3 4 5})  !!TODO

##Declarar estructuras de datos
'("Juan" "María" "Pedro")  !!TODO
#{1 2 3 4 5} 

