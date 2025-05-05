# app_streamlit.py
import streamlit as st
import re

# Funciones de formateo (simplificadas para la web)
def format_text(text, option):
    if option == "MAYÚSCULAS":
        return text.upper()
    elif option == "minúsculas":
        return text.lower()
    elif option == "snake_case":
        return re.sub(r'[^a-zA-Z0-9]+', '_', text).lower()
    elif option == "camelCase":
        words = re.sub(r'[^a-zA-Z0-9]+', ' ', text).split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    # ... (agregar más opciones según necesidad)
    return text

# Interfaz de Streamlit
st.title("📝 Text Formatter Online")
st.write("**Herramienta para convertir texto en diferentes formatos**")

# Input de usuario
input_text = st.text_area("Ingresa tu texto aquí:", "Ejemplo: Hola Mundo")
option = st.selectbox(
    "Selecciona un formato:",
    ["MAYÚSCULAS", "minúsculas", "snake_case", "camelCase"]
)

# Botón de acción
if st.button("Formatear"):
    result = format_text(input_text, option)
    st.code(result, language="text")  # Muestra el resultado en un bloque de código

# Sección adicional
st.markdown("---")
st.write("### Ejemplos rápidos:")
st.write("- `Hola Mundo` → **MAYÚSCULAS**: `HOLA MUNDO`")
st.write("- `Texto Ejemplo` → **snake_case**: `texto_ejemplo`")