import tkinter as tk
from tkinter import messagebox
import re

# Funciones de formateo de texto

def convertir_mayusculas():
    texto = text_input.get("1.0", "end-1c")
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto.upper())

def convertir_minusculas():
    texto = text_input.get("1.0", "end-1c")
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto.lower())

def formato_titulo():
    texto = text_input.get("1.0", "end-1c")
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto.title())

def formato_oracion():
    texto = text_input.get("1.0", "end-1c")
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto.capitalize())

def formato_snake_case():
    texto = text_input.get("1.0", "end-1c")
    texto = re.sub(r'[^a-zA-Z0-9]+', '_', texto).lower()
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto)

def formato_camel_case():
    texto = text_input.get("1.0", "end-1c")
    texto = re.sub(r'[^a-zA-Z0-9]+', ' ', texto).split()
    texto = texto[0].lower() + ''.join(word.capitalize() for word in texto[1:])
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto)

def quitar_espacios():
    texto = text_input.get("1.0", "end-1c")
    texto = re.sub(r'\s+', ' ', texto).strip()
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto)

def quitar_caracteres_especiales():
    texto = text_input.get("1.0", "end-1c")
    texto = re.sub(r'[^a-zA-Z0-9 ]', '', texto)
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto)

def quitar_duplicados():
    texto = text_input.get("1.0", "end-1c")
    texto = " ".join(sorted(set(texto.split()), key=texto.split().index))
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", texto)

def generar_markdown():
    texto = text_input.get("1.0", "end-1c")
    markdown = f"# {texto}"
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", markdown)

def generar_html():
    texto = text_input.get("1.0", "end-1c")
    html = f"<h1>{texto}</h1>"
    text_output.delete("1.0", "end-1c")
    text_output.insert("1.0", html)

def copiar_resultado():
    result = text_output.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(result)
    messagebox.showinfo("Información", "Texto copiado al portapapeles.")

# Crear la interfaz gráfica

root = tk.Tk()
root.title("Formateador de Texto")
root.geometry("500x500")

# Entrada de texto
text_input_label = tk.Label(root, text="Texto de Entrada:")
text_input_label.pack(padx=10, pady=5)
text_input = tk.Text(root, height=10, width=50)
text_input.pack(padx=10, pady=5)

# Botones de formateo
button_upper = tk.Button(root, text="Mayúsculas", command=convertir_mayusculas)
button_upper.pack(pady=5)

button_lower = tk.Button(root, text="Minúsculas", command=convertir_minusculas)
button_lower.pack(pady=5)

button_title = tk.Button(root, text="Formato Título", command=formato_titulo)
button_title.pack(pady=5)

button_sentence = tk.Button(root, text="Formato Oración", command=formato_oracion)
button_sentence.pack(pady=5)

button_snake = tk.Button(root, text="Formato Snake Case", command=formato_snake_case)
button_snake.pack(pady=5)

button_camel = tk.Button(root, text="Formato Camel Case", command=formato_camel_case)
button_camel.pack(pady=5)

button_spaces = tk.Button(root, text="Quitar Espacios Extra", command=quitar_espacios)
button_spaces.pack(pady=5)

button_special_chars = tk.Button(root, text="Quitar Caracteres Especiales", command=quitar_caracteres_especiales)
button_special_chars.pack(pady=5)

button_duplicates = tk.Button(root, text="Quitar Duplicados", command=quitar_duplicados)
button_duplicates.pack(pady=5)

button_markdown = tk.Button(root, text="Generar Markdown", command=generar_markdown)
button_markdown.pack(pady=5)

button_html = tk.Button(root, text="Generar HTML", command=generar_html)
button_html.pack(pady=5)

# Salida de texto
text_output_label = tk.Label(root, text="Texto Formateado:")
text_output_label.pack(padx=10, pady=5)
text_output = tk.Text(root, height=10, width=50)
text_output.pack(padx=10, pady=5)

# Botón para copiar resultado
button_copy = tk.Button(root, text="Copiar Resultado", command=copiar_resultado)
button_copy.pack(pady=20)

root.mainloop()
