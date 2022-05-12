# coding=utf-8
import sys

# Comprobación de seguridad, ejecutar sólo si se reciben 2 argumentos reales
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print('Error - Introduce los argumentos correctamente')
    print('Ejemplo: programa_3.py "Texto" 5')
