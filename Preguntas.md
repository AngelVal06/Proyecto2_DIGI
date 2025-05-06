## **Criterio 6a) Objetivos estratégicos**

**¿Qué objetivos estratégicos específicos de la empresa aborda tu software?**  

Automatización de procesos manuales: Elimina la edición manual de textos (ej: convertir 500 archivos .txt a CSV en segundos).

Estandarización de datos: Garantiza formatos consistentes (snake_case, camelCase) para sistemas downstream.

Reducción de errores humanos: Al evitar cortar/pegar o modificaciones manuales.

**¿Cómo se alinea el software con la estrategia general de digitalización?**

Estrategia "Data First": El software prepara datos para su uso en herramientas de BI (Power BI, Tableau).

Interoperabilidad: Genera outputs compatibles con APIs (JSON), ERPs (CSV) y CMS (HTML).

---

## **Criterio 6b) Áreas de negocio y comunicaciones**

**¿Qué áreas de la empresa (producción, negocio, comunicaciones) se ven más beneficiadas con tu software?**

Producción/Negocio: 
- Procesamiento masivo de datos de proveedores (ej: normalizar nombres de productos).

- Generación de informes estandarizados.

Comunicaciones:

- Creación rápida de contenido web (HTML/Markdown).

- Limpieza de bases de datos de contactos (eliminación de duplicados).

**¿Qué impacto operativo esperas en las operaciones diarias?**

Ahorro de tiempo: Reduce tareas repetitivas de 4 horas → 5 minutos.

Consistencia: Todos los departamentos usan los mismos formatos.

---

## **Criterio 6c) Áreas susceptibles de digitalización**

**¿Qué áreas de la empresa son más susceptibles de ser digitalizadas con tu software?**  
- Digitaliza la edición de CVs (ej: pasar todos a formato título).

- Normaliza nombres de clientes en CRM (ej: "Juan Pérez" → "juan_perez").

**¿Cómo mejorará la digitalización las operaciones en esas áreas?**  

Rastreabilidad: Auditoría de cambios (logs en processed_*).

Escalabilidad: Procesar 1 o 10,000 archivos con igual eficiencia.

---

## **Criterio 6d) Encaje de áreas digitalizadas (AD)**

**¿Cómo interactúan las áreas digitalizadas con las no digitalizadas?**  

Ejemplo: Recibe datos manuales (ej: notas de reuniones en .txt) y los convierte en informes estructurados (.csv) para análisis.

Problema: Sistemas legacy no leen JSON/HTML.

Solución: Exportar a formatos universales (CSV) y usar scripts de conversión puente.

**¿Qué soluciones o mejoras propondrías para integrar estas áreas?** 

API intermedia: Para sistemas que solo aceptan XML.

Plantillas predefinidas: Para áreas con necesidades fijas (ej: contabilidad).

---

## **Criterio 6e) Necesidades presentes y futuras**

**¿Qué necesidades actuales de la empresa resuelve tu software?**  

Unificación de formatos: Ej: 5 departamentos usan 3 formatos distintos para IDs. Y mi proyecto los pasa a un formato en común sin problemas.

---

## **Criterio 6f) Relación con tecnologías**

**¿Qué tecnologías habilitadoras has empleado y cómo impactan en las áreas de la empresa?**  

- Tkinter: Interfaz accesible para no técnicos.

- Expresiones regulares:	Estandarización avanzada (ej: extraer códigos postales de texto libre).

- Python:	Integración con APIs y librerías de análisis (pandas).

**¿Qué beneficios específicos aporta la implantación de estas tecnologías?**  

- Tkinter: Reduce curva de aprendizaje.

- Expresiones regulares:	Precisión del 99.9%.

- Python:	Extensible para necesidades complejas.

---

## **Criterio 6g) Brechas de seguridad**

**¿Qué posibles brechas de seguridad podrían surgir al implementar tu software?**  

Inyección de código: Archivos .txt con comandos maliciosos.

Fuga de datos: Archivos temporales no cifrados

**¿Qué medidas concretas propondrías para mitigarlas?**  

Propondría una función de validación que valide los archivos. 

---

## **Criterio 6h) Tratamiento de datos y análisis**

**¿Cómo se gestionan los datos en tu software y qué metodologías utilizas?**  

Los datos se gestionan bajo un flujo optimizado para procesamiento en memoria, evitando almacenamiento persistente innecesario.

Metodologías: 

- Validación: Tamaño (<10MB), extensiones, y sanitización con re.

- Transformación: Funciones modulares (ej: snake_case, quitar_duplicados).

**¿Qué haces para garantizar la calidad y consistencia de los datos?** 

Tests unitarios: Verifican que "Juan Pérez" → "juan_perez" (snake_case).

Benchmarks: 1,000 archivos procesados en <2 segundos (máx. 10MB cada uno).

