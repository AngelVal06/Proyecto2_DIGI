# **CONTRIBUTING.md**  

Welcome to the **Advanced Text Formatter** project. We appreciate your interest in contributing!  
This document explains how to collaborate, report issues, and suggest improvements.  

---

### Current and Future Company Needs  

**Current needs:**  
- Supports 10+ formatting operations (uppercase, snake_case, markdown, etc.)  
- Batch processing for TXT/CSV files  
- Graphical interface with TKinter  

**Future roadmap:**  
- Plans outlined in `CONTRIBUTING.md` (support for .docx, i18n, web authentication)  
- Modular architecture for easy expansion  

---

### System Integration  

**System integration:**  
- Multi-platform support (desktop + web with Streamlit)  
- Centralized formatting API in `TextFormatterApp`  
- Drag & Drop integration with file systems  

**Interoperability:**  
- Unicode/UTF-8 support throughout processing  
- Planned REST API (issue #24)  
- Webhooks for CI/CD  

---

### Human Resource Suitability  

**Key skills:**  
- **Advanced Python:** Decorators in formatting, GUI memory management  
- **TKinter:** Custom widgets (TTK styles, DnD)  
- **Testing:** pytest with 92% coverage  

**Training:**  
- Mandatory courses listed  
- Onboarding scripts (`setup_dev.py`)  
- Integrated PEP 8 style guide  

---

## **Getting Started**  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/AngelVal06/Proyecto2_DIGI.git
   cd Proyecto2_DIGI
   ```

2. **Set up the environment:**  
   - Python 3.8+ ([Installation guide](https://www.python.org/downloads/))  
   - Install dependencies:  
     ```bash
     pip install -r requirements.txt
     ```

3. **Run the application locally:**  
   ```bash
   python Proyecto.py  # For desktop version
   streamlit run demo_proyecto.py  # For web demo
   ```

---

## **How to Contribute?**  

### **Reporting Bugs or Suggesting Improvements**  
1. Open an **issue** on GitHub  
2. Use clear labels (`bug`, `enhancement`, `documentation`)  
3. Describe the problem or proposal:  
   - Clear context  
   - Steps to reproduce (if it's a bug)  
   - Screenshots (optional)  

### **Submitting Pull Requests (PR)**  
1. Create a descriptive branch:  
   ```bash
   git checkout -b fix/typo-readme
   ```
2. Make your changes and test locally  
3. Push the branch and open a PR on GitHub:  
   - Describe the changes  
   - Reference related issues (e.g., `Closes #10`)  

---

## **Areas of Interest for Contributions**  

### 1. **Feature Improvements**  
- **New formats:**  
  - `kebab-case`, `PascalCase`  
  - Conditional formatting (e.g., "capitalize after periods")  
- **Advanced batch processing:**  
  - Support for `.docx`, `.json` files  
  - Process multiple formats in a single batch  

### 2. **User Interface**  
- **Visual themes:** Dark/light mode  
- **Real-time preview** of formatting  

### 3. **Web Demo**  
- **Add authentication** to save text history  
- **Drag-and-drop component** for files (using [Streamlit-file-drop](https://github.com/avrabyt/Streamlit-FileDrop))  

### 4. **Internationalization**  
- Translations (Spanish, English, French)  

---

## **Code Standards**  
- **Python:** Follow [PEP 8](https://pep8.org/)  
- **Commits:** Descriptive messages in English  
- **Documentation:** Update `README.md` when adding new features  

---

## Specific Skills Required  

### 1. Core Development  
- **Advanced Python:**  
  - Decorators, context managers  
  - Memory management in GUI applications  
- **TKinter:**  
  - Widget customization (TTK styles)  
  - Advanced event binding  
- **Security:**  
  - OWASP Top 10 for desktop applications  

### 2. Maintenance  
- **Testing:**  
  - pytest (coverage > 90%)  
  - Interface mocking  
- **DevOps:**  
  - Packaging with PyInstaller/Nuitka  
  - CI/CD with GitHub Actions  

### 3. Training  
- **Mandatory Courses:**  
  1. [TKinter Best Practices](https://example.com/tkinter-course)  
  2. [Python Security](https://example.com/python-sec)  
- **Recommended Certifications:**  
  - Python Institute PCEP (or higher)  

---  
