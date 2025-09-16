# Autoprint 🖨️

**Autoprint** es un script en Python que permite **imprimir documentos en masa** de manera automática, agregando pausas configurables entre lotes de impresiones.
El objetivo es evitar el sobrecalentamiento del motor de la impresora y prolongar su vida útil, sin necesidad de supervisión constante.

---

## 📑 Índice de contenidos

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Configuración](#configuración)
5. [Ejecución](#ejecución)
6. [Detención](#detención)
7. [Compatibilidad](#compatibilidad)
8. [Disclaimers](#disclaimers)
9. [Licencia](#licencia)
10. [Agradecimientos](#agradecimientos)
11. [Autor](#autor)

---

## 📖 Introducción

Con **Autoprint**, puedes dejar tu computadora encendida mientras el script imprime un gran número de documentos, respetando tiempos de reposo entre lotes para evitar fallos mecánicos o sobrecalentamiento.

Solo necesitas:

* El documento a imprimir.
* Definir cuántas copias quieres por bloque.
* Configurar los tiempos de espera entre bloques y entre impresiones.

💡 *Consejo*: asegúrate de que la impresora tenga papel suficiente antes de iniciar el proceso.

---

## ⚙️ Requisitos

* **Sistema operativo**: Windows (solamente, por ahora).
* **Python**: versión 3.12 o superior.
* **Dependencias**:

  ```bash
  pip install pywin32
  ```

---

## 📥 Instalación

1. Clona este repositorio o descarga el archivo `imprimir_loop.py`.

   ```bash
   git clone https://github.com/GuilloSGit/PythonFolder.git
   cd PythonFolder
   ```
2. Asegúrate de tener Python y las librerías instaladas.
3. Ubica el documento a imprimir en la misma carpeta del script **o** copia su ruta completa.

---

## 🔧 Configuración

Edita el archivo `imprimir_loop.py` y ajusta las siguientes variables:

```python
archivo = "C:\\Users\\[tu usuario]\\Documents\\documento.docx"  # Ruta del documento a imprimir
impresiones_por_bloque = 10   # Número de impresiones por bloque
reposo_segundos = 60          # Tiempo de espera entre bloques (en segundos)
delay_between_prints = 2      # Pausa entre cada impresión (en segundos)
```

---

## ▶️ Ejecución

Ejecuta el script con:

```bash
python imprimir_loop.py
```

---

## ⏹️ Detención

Puedes detener la ejecución en cualquier momento con:

```
Ctrl + C
```

---

## 💻 Compatibilidad

* Actualmente soporta **Windows únicamente** (debido a la dependencia `pywin32`).
* Soporte para otros sistemas operativos podría añadirse en futuras versiones.

---

## ⚠️ Disclaimers

* El autor **no se hace responsable** por el uso que se le dé a este script.
* No se garantiza que funcione con todas las impresoras ni que evite por completo el desgaste del hardware.
* Úsalo bajo tu propia responsabilidad.

---

## 📜 Licencia

Este proyecto se distribuye bajo la licencia [MIT](LICENSE).

---

## 🙏 Agradecimientos

* A mi madre, por la paciencia y la comprensión.

---

## 👤 Autor

* **Guillermo Andrada**
* 📧 [guillermoandrada@gmail.com](mailto:guillermoandrada@gmail.com)
* 📅 *16 de septiembre de 2025*
* 📌 Versión **1.0**
