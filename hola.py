# -*- coding: utf-8 -*-

print 'Ingrese su nombre:'
nombre = raw_input('>>> ')

print 'Ingrese un numero:'
numero = raw_input('>>> ')

sum = 0
for digito in numero:
    sum += int(digito)

print 'Hola {0}, ingresaste {1}, la suma de sus digitos es {2}'.format(nombre, numero, sum)
