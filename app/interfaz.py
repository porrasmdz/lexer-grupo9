import tkinter as tk

def show_text():
    text1.config(state=tk.NORMAL)
    text2.config(state=tk.NORMAL)
    text3.config(state=tk.NORMAL)
    
    text1.delete("1.0", tk.END)
    text2.delete("1.0", tk.END)
    text3.delete("1.0", tk.END)
    
    text1.insert(tk.END, "Texto en el primer cuadro de texto")
    text2.insert(tk.END, "Texto en el segundo cuadro de texto")
    text3.insert(tk.END, "Texto en el tercer cuadro de texto")
    
    text1.config(state=tk.DISABLED)
    text2.config(state=tk.DISABLED)
    text3.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz gráfica con Tkinter")

# Crear cuadros de texto
text1 = tk.Text(root, height=5, width=40)
text2 = tk.Text(root, height=5, width=40)
text3 = tk.Text(root, height=5, width=40)
text4 = tk.Entry(root, width=40)

# Desactivar la edición en los tres primeros cuadros de texto
text1.config(state=tk.DISABLED)
text2.config(state=tk.DISABLED)
text3.config(state=tk.DISABLED)

# Colocar los cuadros de texto en la ventana
text1.pack(pady=10)
text2.pack(pady=10)
text3.pack(pady=10)
text4.pack(pady=10)

# Botón para mostrar texto en los cuadros de texto
btn_show = tk.Button(root, text="Mostrar texto", command=show_text)
btn_show.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()