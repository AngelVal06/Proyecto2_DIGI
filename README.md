# Proyecto2_DIGI

### Nombre del Proyecto: DIGIpROJECT

## 🚀 **Motivación**  
Este proyecto nace para simplificar tareas repetitivas de formateo de texto, como:  
- Convertir mayúsculas/minúsculas.  
- Generar formatos técnicos (`snake_case`, `camelCase`).  
- Limpiar texto (espacios, caracteres especiales, duplicados).  
- Exportar a Markdown/HTML.  
- Procesar **archivos en lote** (ideal para logs, CSVs o bases de datos).  

Está diseñado para **desarrolladores, escritores y analistas de datos** que necesitan normalizar texto rápidamente.  

---

## 🛠 **Instalación y Despliegue**  

### **Requisitos**  
- Python 3.8+ ([Descargar aquí](https://www.python.org/downloads/)).  
- Librerías: `tkinterdnd2` (para drag-and-drop).  

### **Pasos**  
1. **Clonar el repositorio**:  
   ```bash
   git clone https://github.com/AngelVal06/Proyecto2_DIGI.git
   cd Proyecto2_DIGI
   ```

2. **Instalar dependencias**:  
   ```bash
   pip install tkinterdnd2
   ```

3. **Ejecutar la aplicación**:  
   ```bash
   python Proyecto.py
   ```

### **Ejecutable (opcional)**  
Para crear un archivo `.exe` (Windows) o `.app` (macOS):  
```bash
pip install pyinstaller
pyinstaller --onefile --windowed Proyecto.py
```
*(Los binarios se generan en `dist/`)*.  

---

## 🎯 **Ejemplos de Uso**  

### **1. Formateo Básico**  
- **Convertir a mayúsculas**:  
  ```text
  Entrada: "hola mundo"  
  Salida: "HOLA MUNDO"
  ```
  ![image](https://github.com/user-attachments/assets/5b8d4870-8c8b-4008-83a8-6adef06170a0)

- **Generar `snake_case`**:  
  ```text
  Entrada: "Texto de Prueba"  
  Salida: "texto_de_prueba"
  ```
  ![image](https://github.com/user-attachments/assets/2e344def-fd15-4a8b-a889-a97db7bbf020)


### **2. Procesamiento por Lotes**  
1. Arrastra archivos `.txt` o `.csv` a la pestaña **"Procesar Archivos"**.  
2. Selecciona un formato (ej: "Quitar Espacios").  
3. Elige una carpeta de salida.  
4. Los archivos procesados se guardarán como `processed_*`.  


![image](https://github.com/user-attachments/assets/9e2fe153-5552-46e5-807f-22f78a47714f)
![image](https://github.com/user-attachments/assets/c9929cb4-0f65-4e7c-a0f7-88987d8a4f28) ![image](https://github.com/user-attachments/assets/6ea9fe96-2384-49ae-8a8f-2e79301cf334)

---

## 🔗 **Enlace a la Demo**
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://proyecto2digi-cgdsk5knpkhchzpxhrsdw2.streamlit.app/)

