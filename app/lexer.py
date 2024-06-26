from ply.lex import lex

reserved = {
    "def": "DEF",
    "if": "IF",
    "fn": "FN",
    "quote": "QUOTE",
    "try": "TRY",
    "defn": "DEFN",
    "loop": "LOOP",
    "var": "VAR",
    "catch": "CATCH",
    "let": "LET",
    "do": "DO",
    "recur": "RECUR",
    "throw": "THROW",
    "finally": "FINALLY",
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "mod": "MOD",
    "print":"PRINT",
    "println":"PRINTLN",
    "while" : "WHILE",
    "set": "SET",
    "list": "LIST",
    "range": "RANGE",
    "for": "FOR"
}
tokens = (
    'INT',
    'FLOAT',
    'STRING',
    'BOOLEAN',
    'ID',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACK',
    'RBRACK',
    'LBRACE',
    'RBRACE',
    'HASH',
    'HASHSET',
    'LISTSTART',
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_EQUAL',
    'LESS_EQUAL',
    'COMILLA',
)  + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*\s'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_HASH = r'\#'
t_HASHSET=r'\#\{'
t_LISTSTART=r'\'\('
t_EQUAL = r'='
t_NOT_EQUAL = r'not='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_COMILLA = r'\''

# Regla para identificadores y palabras reservadas
def t_ID(t):
    r'[\*!\?\-_a-zA-Z][\*!\?\-_a-zA-Z0-9]*'
    # r'[\*[^\s]!\?\-_a-zA-Z][\*[^\s]!\?\-_a-zA-Z0-9]*|\*[^\s]+[\*[^\s]!\?\-_a-zA-Z0-9]*'

    t.type = reserved.get(t.value, 'ID')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t


t_STRING = r'\"([^\\\n]|(\\.))*?\"'

def t_FLOAT(t):
    r'\d+\.\d+([eE][-+]?\d+)?'
    t.value = float(t.value)
    return t


def t_BOOLEAN(t):
    r'\b(true|false)\b'
    t.value = True if t.value == "true" else False
    return t

def t_COMMENT_SINGLE(t):
    r';[^\n]*'
    pass  # Los comentarios de una sola línea se ignoran completamente

# Regla para comentarios de múltiples líneas (simulación)
def t_COMMENT_MULTI(t):
    r'\#_\{[^\}]*\}'
    pass  # L


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex()

def test_lexer():
    #Alg 1
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
    '''
        #Alg 2
    #data =  '''
    #     ; Numero es par o impar
    # (defn determinar-paridad [numero]
    #   (if (integer? numero)
    #     (if (zero? (mod numero 2))
    #       "es par"
    #       "es impar")
    #     (str numero " no es un número entero")))
    #     '''
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No más entrada
  