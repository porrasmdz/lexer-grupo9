import tkinter as tk
import sv_ttk
from tkinter import ttk

class ClojureApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        #Config
        self.apply_settings()
        #UI
        self.append_menu_component()
        self.append_code_evaluation_column()
        self.append_ply_analyzers_column()
    
    #====================================================
    #========GUI Components==============================
    #====================================================    
    def apply_settings(self):
        #Basics
        self.title("Proyecto Clojure - Grupo 9 | Alfredo Porras, Stiven Rivera")
        self.option_add("*tearOff", False)
        self.geometry("800x600")  
        self.resizable(width=True, height=True)  
        
        
        sv_ttk.set_theme("dark")
        #Title icon
        self.iconbitmap("app/assets/favicon.ico")  

    def append_menu_component(self):
        menu_bar = tk.Menu(self)
        
        # ==============Archive==============
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_command(label="Guardar", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)
        
        # ==============Help==============
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self.show_about)
        menu_bar.add_cascade(label="Ayuda", menu=help_menu)
        
        self.config(menu=menu_bar)

    def append_code_evaluation_column(self):
        frame_code = ttk.Frame(self, width=500)
        frame_code.pack(side="left", fill="both", padx=10, pady=10)
        frame_code.pack_propagate(False)

        self.label_code = ttk.Label(frame_code, text="Código")
        self.label_code.pack(anchor="w")
        
        self.code_string= tk.StringVar(value="Ingrese su código aquí y pulse CTRL + ENTER para compilar...")
        self.entry_code = ttk.Entry(frame_code, textvariable=self.code_string)
        self.entry_code.pack(anchor="w", fill="x", pady=5)
        self.entry_code.focus()
        
        self.button = ttk.Button(frame_code, text="Compilar Código", style="Accent.TButton", command=self.compile_code)
        self.button.pack(pady=10, anchor="w")

        self.label_result = ttk.Label(frame_code, text="Resultado")
        self.label_result.pack(anchor="w", pady=(10,0))
        self.text_result = ttk.Entry(frame_code, width=40, state='disabled')
        self.text_result.pack(anchor="w",pady=5,  fill="x")
        self.entry_code.bind("<Control-Return>", self.compile_code)

    def append_ply_analyzers_column(self):
        frame_analyzers = ttk.Frame(self)
        frame_analyzers.pack(side="right", fill="y", padx=10, pady=10)

        self.label1 = ttk.Label(frame_analyzers, text="Label 1")
        self.label1.pack(anchor="w")
        
        self.text1 = ttk.Entry(frame_analyzers, width=80, state='disabled')
        self.text1.pack(pady=5)
        
        self.label2 = ttk.Label(frame_analyzers, text="Label 2")
        self.label2.pack(anchor="w", pady=(10, 0))
        
        self.text2 = ttk.Entry(frame_analyzers, width=80, state='disabled')
        self.text2.pack(pady=5)
        
        self.label3 = ttk.Label(frame_analyzers, text="Label 3")
        self.label3.pack(anchor="w", pady=(10, 0))
        
        self.text3 = ttk.Entry(frame_analyzers, width=80, state='disabled')
        self.text3.pack(pady=5)

    #====================================================
    #========Business Logic functions====================
    #====================================================    
    def open_file(self):
        pass  # Lógica para abrir un archivo
    
    def save_file(self):
        pass  # Lógica para guardar un archivo
    
    def show_about(self):
        pass  # Mostrar información sobre la aplicación
    def compile_code(self, event=None):
        # Función para compilar el código (acción del botón)
        code_to_compile = self.code_string.get()
        print(f"El codigo es:\nclojure> {code_to_compile}")
        # Aquí puedes poner la lógica para compilar el código