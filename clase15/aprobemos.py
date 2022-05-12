# coding=utf-8
import sys

if len(sys.argv) == 3:
  if (int(sys.argv[1]) > 0 and int(sys.argv[1]) <= 10) and (int(sys.argv[2]) > 0 and int(sys.argv[2]) <= 10):
    nota1 = int(sys.argv[1])
    nota2 = int(sys.argv[2])
    
    if nota1 >= 7 and nota2 >= 7:
      print('Promocionado')
    elif nota1 >= 4 and nota2 >= 4:
      print('Aprobado, debe rendir final')
    elif nota1 <= 4 and nota2 >= 4:
      print('Desaprobado, debe recuperar el primer parcial')
    elif nota1 >= 4 and nota2 <= 4:
      print('Desaprobado, debe recuperar el segundo parcial')
    elif nota1 <= 4 and nota2 <= 4:
      print('Desaprobó ambos parciales, debe recursar')
    else:
      print('Ingrese números entre 0 y 10')
  else:
    print('Está fuera de rango')
else:
  print('Argumentos ingresados incorrectamente')
  print('Debe ingresar 2 argumentos enteros entre 0 y 10')
