import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import re
import os
from tkinterdnd2 import TkinterDnD, DND_FILES

class TextFormatterApp(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Advanced Text Formatter")
        self.geometry("700x800")
        self.configure(bg="#f0f0f0")
        self.resizable(True, True)
        
        # Estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 9), padding=5)
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', font=('Arial', 9, 'bold'), padding=[10, 5])
        
        self.create_widgets()
        
    def create_widgets(self):
        # Notebook para pestañas
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña de formato simple
        simple_tab = ttk.Frame(notebook)
        notebook.add(simple_tab, text="Formatear Texto")
        
        # Pestaña de procesamiento por lotes
        batch_tab = ttk.Frame(notebook)
        notebook.add(batch_tab, text="Procesar Archivos")
        
        # Widgets para la pestaña de formato simple
        self.create_simple_tab(simple_tab)
        
        # Widgets para la pestaña de procesamiento por lotes
        self.create_batch_tab(batch_tab)
    
    def create_simple_tab(self, parent):
        # Frame de entrada
        input_frame = ttk.Frame(parent)
        input_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Label(input_frame, text="Texto de Entrada:").pack(anchor=tk.W)
        
        self.text_input = tk.Text(input_frame, height=10, width=80, font=('Arial', 10), 
                                 wrap=tk.WORD, padx=5, pady=5, bd=2, relief=tk.GROOVE)
        self.text_input.pack(fill=tk.X, pady=(0, 10))
        
        # Frame de botones
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Primera fila de botones
        row1 = ttk.Frame(button_frame)
        row1.pack(fill=tk.X, pady=2)
        
        ttk.Button(row1, text="MAYÚSCULAS", command=self.convertir_mayusculas, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row1, text="minúsculas", command=self.convertir_minusculas, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row1, text="Formato Título", command=self.formato_titulo, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        # Segunda fila de botones
        row2 = ttk.Frame(button_frame)
        row2.pack(fill=tk.X, pady=2)
        
        ttk.Button(row2, text="Formato Oración", command=self.formato_oracion, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row2, text="snake_case", command=self.formato_snake_case, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row2, text="camelCase", command=self.formato_camel_case, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        # Tercera fila de botones
        row3 = ttk.Frame(button_frame)
        row3.pack(fill=tk.X, pady=2)
        
        ttk.Button(row3, text="Quitar Espacios", command=self.quitar_espacios, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row3, text="Quitar Especiales", command=self.quitar_caracteres_especiales, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row3, text="Quitar Duplicados", command=self.quitar_duplicados, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        # Cuarta fila de botones
        row4 = ttk.Frame(button_frame)
        row4.pack(fill=tk.X, pady=2)
        
        ttk.Button(row4, text="Generar Markdown", command=self.generar_markdown, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row4, text="Generar HTML", command=self.generar_html, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        ttk.Button(row4, text="Copiar Resultado", command=self.copiar_resultado, 
                  style='TButton').pack(side=tk.LEFT, padx=2, expand=True, fill=tk.X)
        
        # Frame de salida
        output_frame = ttk.Frame(parent)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(output_frame, text="Texto Formateado:").pack(anchor=tk.W)
        
        self.text_output = tk.Text(output_frame, height=15, width=80, font=('Arial', 10), 
                                 wrap=tk.WORD, padx=5, pady=5, bd=2, relief=tk.GROOVE)
        self.text_output.pack(fill=tk.BOTH, expand=True)
        
        # Configurar scrollbar
        scrollbar = ttk.Scrollbar(output_frame, command=self.text_output.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_output.config(yscrollcommand=scrollbar.set)
    
    def create_batch_tab(self, parent):
        # Frame de instrucciones
        instructions_frame = ttk.Frame(parent)
        instructions_frame.pack(fill=tk.X, padx=10, pady=(10, 5))
        
        ttk.Label(instructions_frame, 
                 text="Arrastra y suelta archivos .txt o .csv aquí, o haz clic en 'Seleccionar Archivos'").pack()
        
        # Frame de área de arrastre
        drop_frame = ttk.Frame(parent, height=100, relief=tk.GROOVE)
        drop_frame.pack(fill=tk.X, padx=10, pady=5)
        drop_frame.pack_propagate(False)
        
        self.drop_label = ttk.Label(drop_frame, text="Arrastra archivos aquí", 
                                   foreground="gray", font=('Arial', 10, 'italic'))
        self.drop_label.pack(expand=True)
        
        # Configurar drag and drop
        drop_frame.drop_target_register(DND_FILES)
        drop_frame.dnd_bind('<<Drop>>', self.on_drop)
        
        # Frame de botones
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Button(button_frame, text="Seleccionar Archivos", 
                  command=self.select_files).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Limpiar Lista", 
                  command=self.clear_file_list).pack(side=tk.LEFT, padx=2)
        
        # Frame de lista de archivos
        list_frame = ttk.Frame(parent)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.file_listbox = tk.Listbox(list_frame, height=8, font=('Arial', 9), 
                                     selectmode=tk.EXTENDED, bd=2, relief=tk.GROOVE)
        self.file_listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Frame de opciones de formato
        format_frame = ttk.Frame(parent)
        format_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(format_frame, text="Formato a aplicar:").pack(side=tk.LEFT, padx=(0, 10))
        
        self.format_var = tk.StringVar()
        self.format_combobox = ttk.Combobox(format_frame, textvariable=self.format_var, 
                                          values=["MAYÚSCULAS", "minúsculas", "Formato Título", 
                                                 "Formato Oración", "snake_case", "camelCase",
                                                 "Quitar Espacios", "Quitar Especiales", "Quitar Duplicados"],
                                          state="readonly", width=15)
        self.format_combobox.pack(side=tk.LEFT, padx=(0, 10))
        self.format_combobox.current(0)
        
        ttk.Button(format_frame, text="Procesar Archivos", 
                  command=self.process_files).pack(side=tk.LEFT)
    
    # Funciones de formateo de texto (las mismas que antes pero como métodos de clase)
    def convertir_mayusculas(self):
        texto = self.text_input.get("1.0", "end-1c")
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto.upper())

    def convertir_minusculas(self):
        texto = self.text_input.get("1.0", "end-1c")
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto.lower())

    def formato_titulo(self):
        texto = self.text_input.get("1.0", "end-1c")
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto.title())

    def formato_oracion(self):
        texto = self.text_input.get("1.0", "end-1c")
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto.capitalize())

    def formato_snake_case(self):
        texto = self.text_input.get("1.0", "end-1c")
        texto = re.sub(r'[^a-zA-Z0-9]+', '_', texto).lower()
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto)

    def formato_camel_case(self):
        texto = self.text_input.get("1.0", "end-1c")
        texto = re.sub(r'[^a-zA-Z0-9]+', ' ', texto).split()
        texto = texto[0].lower() + ''.join(word.capitalize() for word in texto[1:])
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto)

    def quitar_espacios(self):
        texto = self.text_input.get("1.0", "end-1c")
        texto = re.sub(r'\s+', ' ', texto).strip()
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto)

    def quitar_caracteres_especiales(self):
        texto = self.text_input.get("1.0", "end-1c")
        texto = re.sub(r'[^a-zA-Z0-9 ]', '', texto)
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto)

    def quitar_duplicados(self):
        texto = self.text_input.get("1.0", "end-1c")
        texto = " ".join(sorted(set(texto.split()), key=texto.split().index))
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", texto)

    def generar_markdown(self):
        texto = self.text_input.get("1.0", "end-1c")
        markdown = f"# {texto}"
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", markdown)

    def generar_html(self):
        texto = self.text_input.get("1.0", "end-1c")
        html = f"<h1>{texto}</h1>"
        self.text_output.delete("1.0", "end-1c")
        self.text_output.insert("1.0", html)

    def copiar_resultado(self):
        result = self.text_output.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(result)
        messagebox.showinfo("Información", "Texto copiado al portapapeles.")
    
    # Funciones para el procesamiento por lotes
    def on_drop(self, event):
        files = self.tk.splitlist(event.data)
        valid_files = [f for f in files if f.lower().endswith(('.txt', '.csv'))]
        
        if not valid_files:
            messagebox.showwarning("Advertencia", "Solo se aceptan archivos .txt o .csv")
            return
        
        for file in valid_files:
            if file not in self.file_listbox.get(0, tk.END):
                self.file_listbox.insert(tk.END, file)
    
    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Seleccionar archivos",
            filetypes=(("Archivos de texto", "*.txt"), ("Archivos CSV", "*.csv"), ("Todos los archivos", "*.*"))
        )
        
        if files:
            for file in files:
                if file.lower().endswith(('.txt', '.csv')) and file not in self.file_listbox.get(0, tk.END):
                    self.file_listbox.insert(tk.END, file)
    
    def clear_file_list(self):
        self.file_listbox.delete(0, tk.END)
    
    def process_files(self):
        if self.file_listbox.size() == 0:
            messagebox.showwarning("Advertencia", "No hay archivos seleccionados")
            return
        
        format_func = {
            "MAYÚSCULAS": self.convertir_mayusculas,
            "minúsculas": self.convertir_minusculas,
            "Formato Título": self.formato_titulo,
            "Formato Oración": self.formato_oracion,
            "snake_case": self.formato_snake_case,
            "camelCase": self.formato_camel_case,
            "Quitar Espacios": self.quitar_espacios,
            "Quitar Especiales": self.quitar_caracteres_especiales,
            "Quitar Duplicados": self.quitar_duplicados
        }.get(self.format_var.get())
        
        if not format_func:
            messagebox.showerror("Error", "Formato no válido")
            return
        
        output_dir = filedialog.askdirectory(title="Seleccionar carpeta de salida")
        if not output_dir:
            return
        
        success_count = 0
        for i in range(self.file_listbox.size()):
            file_path = self.file_listbox.get(i)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Usar el text_input y text_output como buffers
                self.text_input.delete("1.0", tk.END)
                self.text_input.insert("1.0", content)
                format_func()
                processed_content = self.text_output.get("1.0", tk.END)
                
                # Guardar el archivo procesado
                filename = os.path.basename(file_path)
                output_path = os.path.join(output_dir, f"processed_{filename}")
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                
                success_count += 1
            except Exception as e:
                messagebox.showerror("Error", f"Error procesando {file_path}:\n{str(e)}")
        
        messagebox.showinfo("Proceso completado", 
                          f"Se procesaron {success_count} de {self.file_listbox.size()} archivos.\n"
                          f"Guardados en: {output_dir}")

if __name__ == "__main__":
    app = TextFormatterApp()
    app.mainloop()