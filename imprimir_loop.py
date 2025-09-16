import time
import win32com.client as win32
from datetime import datetime, timedelta

# ---------- CONFIG ----------
archivo = r"C:\Users\guill\Desktop\invit.docx"
impresiones_por_bloque = 10
reposo_segundos = 300               # 5 minutos
delay_between_prints = 10            # segundos entre cada impresión
# ----------------------------

def mostrar_tiempo_restante(segundos_restantes):
    """Muestra el tiempo restante en un formato legible en español con horas, minutos y segundos."""
    horas = segundos_restantes // 3600
    minutos = (segundos_restantes % 3600) // 60
    segundos = segundos_restantes % 60
    
    if horas > 0:
        return f"Tiempo restante: {minutos:02d}m {segundos:02d}s"
    elif minutos > 0:
        return f"Tiempo restante: {minutos}m {segundos:02d}s"
    else:
        return f"Tiempo restante: {segundos}s"

# Abrir Word
word = win32.Dispatch("Word.Application")
word.Visible = False

# Abrir documento (una sola vez)
doc = word.Documents.Open(archivo, ReadOnly=True)

try:
    while True:
        print(f"\nIniciando bloque de {impresiones_por_bloque} impresiones...")
        
        # Imprimir el bloque actual
        for i in range(impresiones_por_bloque):
            doc.PrintOut(Background=False)
            print(f"Impresión nº {i+1} enviada a la cola de impresión.")
            time.sleep(delay_between_prints)
        
        # Mostrar tiempo de reposo
        print(f"\nEsperando {reposo_segundos // 60} minutos antes del próximo bloque...")
        
        # Iniciar cuenta regresiva
        tiempo_inicio = datetime.now()
        tiempo_fin = tiempo_inicio + timedelta(seconds=reposo_segundos)
        
        while datetime.now() < tiempo_fin:
            segundos_restantes = int((tiempo_fin - datetime.now()).total_seconds()) + 1
            print(f"\r{mostrar_tiempo_restante(segundos_restantes)}    ", end="", flush=True)
            time.sleep(1)
        
        print("\nReiniciando impresiones...")
        
except KeyboardInterrupt:
    print("\nDetenido manualmente con Ctrl+C.")

finally:
    doc.Close(False)
    word.Quit()
