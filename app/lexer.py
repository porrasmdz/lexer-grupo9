from ply.lex import lex

reserved = {
    "def": "DEF",
    "if": "IF",
    "fn": "FN",
    "quote": "QUOTE",
    "try": "TRY",
    "defn": "DEFN",
    "else": "ELSE",
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
    "println":"PRINTLN"
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
    'COMMENT_SINGLE',
    'COMMENT_MULTI',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_EQUAL',
    'LESS_EQUAL',
)  + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACK = r'\['
t_RBRACK = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_HASH = r'\#'
t_EQUAL = r'='
t_NOT_EQUAL = r'not='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='

# Regla para identificadores y palabras reservadas
def t_ID(t):
    r'[\*!\?\-_a-zA-Z][\*!\?\-_a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t


t_STRING = r'\"([^\\\n]|(\\.))*?\"'

def t_FLOAT(t):
    r'\d+\.\d+'
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
    r'\#\{[^\}]*\}'
    pass  # L


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex()