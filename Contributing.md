
# 📌 **CONTRIBUTING.md**  

Bienvenido/a al proyecto **Advanced Text Formatter**. ¡Apreciamos tu interés en contribuir!  
Este documento explica cómo colaborar, reportar issues, y sugerir mejoras.  

---

## **Primeros Pasos**  

1. **Clona el repositorio**:  
   ```bash
   git clone https://github.com/AngelVal06/Proyecto2_DIGI.git
   cd Proyecto2_DIGI
   ```

2. **Configura el entorno**:  
   - Python 3.8+ ([Guía de instalación](https://www.python.org/downloads/)).  
   - Instala dependencias:  
     ```bash
     pip install -r requirements.txt
     ```

3. **Ejecuta la aplicación localmente**:  
   ```bash
   python Proyecto.py  # Para la versión desktop
   streamlit run demo_proyecto.py  # Para la demo web
   ```

---

## **¿Cómo Contribuir?**  

###  **Reportar Errores o Sugerir Mejoras**  
1. Abre un **issue** en GitHub.  
2. Usa etiquetas claras (`bug`, `enhancement`, `documentation`).  
3. Describe el problema o propuesta:  
   - Contexto claro.  
   - Pasos para reproducir (si es un bug).  
   - Capturas de pantalla (opcional).  

### **Enviar Pull Requests (PR)**  
1. Crea una rama descriptiva:  
   ```bash
   git checkout -b fix/typo-readme
   ```
2. Realiza tus cambios y prueba localmente.  
3. Sube la rama y abre un PR en GitHub:  
   - Describe los cambios.  
   - Referencia issues relacionados (ej: `Closes #10`).  

---

## **Áreas de Interés para Contribuciones**  

### 1. **Mejoras de Funcionalidad**  
- ✅ **Nuevos formatos**:  
  - `kebab-case`, `PascalCase`.  
  - Formateo condicional (ej: "capitalizar después de puntos").  
- ✅ **Procesamiento por lotes avanzado**:  
  - Soporte para archivos `.docx`, `.json`.  
  - Procesar múltiples formatos en un solo lote.  

### 2. **Interfaz de Usuario**  
- ✅ **Temas visuales**: Modo oscuro/light.  
- ✅ **Previsualización en tiempo real** del formateo.  

### 3. **Demo Web**  
- ✅ **Añadir autenticación** para guardar historial de textos.  
- ✅ **Componente de arrastrar/soltar** archivos (con [Streamlit-file-drop](https://github.com/avrabyt/Streamlit-FileDrop)).  

### 4. **Internacionalización**  
- ✅ Traducciones (español, inglés, francés).  

---

## ⚠️ **Estándares de Código**  
- **Python**: Sigue [PEP 8](https://pep8.org/).  
- **Commits**: Mensajes descriptivos en inglés.  
- **Documentación**: Actualiza el `README.md` si añades nuevas funciones.  

---

## Habilidades Específicas Requeridas

### 1. Desarrollo Principal
- **Python Avanzado**:
  - Decoradores, context managers.
  - Manejo de memoria en aplicaciones GUI.
- **TKinter**:
  - Customización de widgets (TTK styles).
  - Event binding avanzado.
- **Seguridad**:
  - OWASP Top 10 para aplicaciones desktop.

### 2. Mantenimiento
- **Testing**:
  - pytest (coverage > 90%).
  - Mocking de interfaces.
- **DevOps**:
  - Empaquetado con PyInstaller/Nuitka.
  - CI/CD con GitHub Actions.

### 3. Capacitación
- **Cursos Obligatorios**:
  1. [TKinter Best Practices](https://example.com/tkinter-course)
  2. [Python Security](https://example.com/python-sec)
- **Certificaciones Recomendadas**:
  - Python Institute PCEP (o superior).
---

