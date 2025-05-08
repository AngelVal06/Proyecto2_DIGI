
---

# Project2_DIGI  

### Project Name: Advanced Text Formatter 

## **Motivation**  
This project was created to simplify repetitive text formatting tasks, such as:  
- Converting uppercase/lowercase.  
- Generating technical formats (`snake_case`, `camelCase`).  
- Cleaning text (spaces, special characters, duplicates).  
- Exporting to Markdown/HTML.  
- **Batch processing files** (ideal for logs, CSVs, or databases).  

It is designed for **developers, writers, and data analysts** who need to quickly normalize text.  

---  

## **Installation and Deployment**  

### **Requirements**  
- Python 3.8+ ([Download here](https://www.python.org/downloads/)).  
- Libraries: `tkinterdnd2` (for drag-and-drop).  

### **Steps**  
1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/AngelVal06/Proyecto2_DIGI.git  
   cd Proyecto2_DIGI  
   ```  

2. **Install dependencies**:  
   ```bash  
   pip install tkinterdnd2  
   ```  

3. **Run the application**:  
   ```bash  
   python Proyecto.py  
   ```  

### **Executable (optional)**  
To create an `.exe` (Windows) or `.app` (macOS) file:  
```bash  
pip install pyinstaller  
pyinstaller --onefile --windowed Proyecto.py  
```  
*(Binaries are generated in `dist/`)*.  

---  

## **Usage Examples**  

### **1. Basic Formatting**  
- **Convert to uppercase**:  
  ```text  
  Input: "hola mundo"  
  Output: "HOLA MUNDO"  
  ```  
  ![image](https://github.com/user-attachments/assets/5b8d4870-8c8b-4008-83a8-6adef06170a0)  

- **Generate `snake_case`**:  
  ```text  
  Input: "Texto de Prueba"  
  Output: "texto_de_prueba"  
  ```  
  ![image](https://github.com/user-attachments/assets/2e344def-fd15-4a8b-a889-a97db7bbf020)  

### **2. Batch Processing**  
1. Drag and drop `.txt` or `.csv` files into the **"Process Files"** tab.  
2. Select a format (e.g., "Remove Spaces").  
3. Choose an output folder.  
4. Processed files will be saved as `processed_*`.  

![image](https://github.com/user-attachments/assets/9e2fe153-5552-46e5-807f-22f78a47714f)  
![image](https://github.com/user-attachments/assets/c9929cb4-0f65-4e7c-a0f7-88987d8a4f28) ![image](https://github.com/user-attachments/assets/6ea9fe96-2384-49ae-8a8f-2e79301cf334)  

---  

## **Demo Link**  
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://proyecto2digi-cgdsk5knpkhchzpxhrsdw2.streamlit.app/)  

## **Technologies Used**  
- **Python 3.8+**: Primary language.  
- **TKinter**: Graphical interface.  
- **tkinterdnd2**: Drag-and-drop support.  
- **Regular expressions (re)**: For text transformation.  
- **PyInstaller**: For generating executables.  

---

## **DevLog:** 
In this section, I will write down each day I worked on the project and what I did that day.

**March 1st:** On this day, I improved the code by fixing bugs and adding more functions. I also created the demo program for the code.

**March 2nd:** On this day, I wrote the README and the `contributing.md` file.

**March 3rd:** I wrote the code documentation as well as the documentation using the `pdoc` tool. I also created the license.

**March 4th:** On this day, I checked all the project criteria to see what I was missing and what was done correctly. I also completed the DevLog and answered the questions.



