### Autoprint

Imprime documentos en masa con un reposo entre impresiones.

## Índice de contenidos

1. [Índice de contenidos](#índice-de-contenidos)
2. [Introducción](#introducción)
3. [Cómo configurar](#cómo-configurar)
4. [Cómo ejecutar](#cómo-ejecutar)
5. [Cómo detener](#cómo-detener)
6. [Dispositivos compatibles](#dispositivos-compatibles)
7. [Disclaimers](#disclaimers)
8. [Licencia](#licencia)
9. [Agradecimientos](#agradecimientos)
10. [Contacto](#contacto)


## Introducción

La idea es que no se sobrecaliente el motor de impresión generando pérdidas. Configuras el número de impresiones por bloque y el reposo entre impresiones. Puedes dejar la computadora encendida, y el script se encargará de imprimir los documentos en masa. El detalle, sería dejar la cantidad de papel suficiente para que el script pueda imprimir todos los documentos.

## Cómo configurar

1. Encontrar el path del documento a imprimir y copiarlo, o ponerlo en la misma carpeta que el script. Por ejemplo, si el documento está en `C:\Users\guill\Documents\documento.docx`, copia el path y pégalo en la línea 6 del script.

> Necesitas tener instalado Python 3.12 o superior. Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).

> Este script requiere la librería `pywin32`. Puedes instalarla con `pip install pywin32`.

> Puedes correr el script en Windows solamente (por ahora).

2. Configurar los parámetros del script.

> En la línea 6 del script, cambia el valor de `archivo` por el path del documento a imprimir.

> En la línea 7 del script, cambia el valor de `impresiones_por_bloque` por el número de impresiones por bloque.

> En la línea 8 del script, cambia el valor de `reposo_segundos` por el número de segundos de reposo entre impresiones.

> En la línea 9 del script, cambia el valor de `delay_between_prints` por el número de segundos de delay entre impresiones.

## Cómo ejecutar

> Puedes ejecutar el script con `python imprimir_loop.py`.

## Cómo detener

> Puedes detener el script con `Ctrl+C`.

## Dispositivos compatibles

> Puedes correr el script en Windows solamente (por ahora).

## Disclaimers

> No me hago responsable por el uso que le des a este script. Ni por el resultado que obtengas.

> No me hago responsable por el daño que pueda causarle a su computadora o impresora.

## Licencia

> Este software es de uso gratuito y está disponible bajo la [licencia MIT](LICENSE).

## Agradecimientos

> Gracias a mi madre, por la paciencia y la comprensión.

## Contacto

> Si tienes alguna pregunta, puedes contactarme en [mi correo electrónico](mailto:guillermo@guillermo.com).

## Autor

> Guillermo Andrada

## Fecha

> 16 de septiembre de 2025
> Versión 1.0
