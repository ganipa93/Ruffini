#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Autor: Gabriel Palazzo.")
	print ("Cuantos terminos tiene: ")
	print ("\t1 - Presione (1) Notas del autor)")
	print ("\t2 - Presione (2) si tiene dos terminos, (sin contar el independiente)")
	print ("\t3 - Presione (3) si tiene tres terminos, (sin contar el independiente)")
	print ("\t4 - Presione (4) si tiene cuatro terminos, (sin contar el independiente)")
	print ("\t5 - Presione (5) para salir")
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >>:  ")
 
 #opcion 1
	if opcionMenu=="1":
		import msvcrt
		print ("")
		print ("*Solo se aceptan numeros enteros*")
		msvcrt.getch()
 #opcion 2
	elif opcionMenu=="2":
		import msvcrt
		print ("")
		a = int(input("x2: "))
		b = int(input("x3: "))
		c = int(input("termino Independiente: "))
 
		f = int(input("Valor Madre:"))
		g = a
 
		b_1 = int(f*g)
		b_r = int(b+b_1)
		c_1 = int(f*b_r)
		c_r = int(c+c_1)
 
		print("Cociente: ", int(g), int(b_r))
		print("Resto: ", int(c_r))
 
		f_1 = int(input("Valor Madre segundo: "))
		b_2 = int(f_1*g)
		b_2r = int(b_r+b_2)
 
		print(g)
		print("Resto: ", int(b_2r))
		msvcrt.getch()
 
 	#opcion 3
	if opcionMenu=="3":
		import msvcrt
		print ("")
		a = int(input("x^3: "))
		b = int(input("x^2: "))
		c = int(input("x: "))
		d = int(input("Termino independiente: "))
 
		f = int(input("Valor Madre: "))
 
		g = a
		b_1 = int(f*g)
		b_r = int(b+b_1)
		c_1 = int(f*b_r)
		c_r = int(c+c_1)
		d_1 = int(f*c_r)
		d_r = int(d+d_1)
 
		print(int(g), int(b_r), int(c_r))
		print(int(d_r))
		#segunda
		f_1 = int(input("segundo valor madre : "))
 
		b_2 = int(f_1*g)
		b_r2 = int(b_r+b_2)
		c_2 = int(f_1*b_r2)
		c_r2 = int(c_r+c_2)
 
		print(int(g),int(b_r2))
		print(int(c_r2))
		#tercero
		f_2 = int(input("tercer valor madre: "))
		b_3 = int(f_2*g)
		b_r3 = int(b_r2+b_3)
		print(int(g))
		print(b_r3)
		msvcrt.getch()
 
 #opcion 4
	elif opcionMenu=="4":
		import msvcrt
		print ("")
		a = input("Valor que sustituye a x^4: ")
		b = input("Valor que sustituye a x^3: ")
		c = input("Valor que sustituye a x^2: ")
		d = input("Valor que sustituye a x: ")
		e = input("Termino Independiente: ")
 
		f = input("Valor Madre: ")
 
		g = int(a)
		h = int(f)*int(g)
		i = int(b)+int(h)
		j = int(f)*int(i)
		k = int(c)+int(j)
		l = int(f)*int(k)
		m = int(d)+int(l)
		n = int(f)*int(m)
		resto = int(e)+int(n)
 
		print("Cociente: ", g, i, k, m)
		print("Resto: ", resto)
 
		#segundo valor
		f_1 = int(input("Segundo valor para ruffini: "))
 
		i_1 = int(f_1*g)
		i_r = int(i+i_1)
		k_1 = int(f_1*i_r)
		k_r = int(k+k_1)
		m_1 = int(f_1*k_r)
		m_r = int(m+m_1)
 
		print("Cociente_2: ",int(g),int(i_r),int(k_r))
		print("Resto_2: ", int(m_r))
 
		#tercero
		f_2 = int(input("Tercer valor para ruffini: "))
 
		i_r2 = int(f_2*g)
		i_rtotal = int(i_r+i_r2)
		k_r2 = int(f_2*i_rtotal)
		k_rtotal = int(k_r+k_r2)
 
		print("Cociente_3: ", int(g), int(i_rtotal))
		print("Resto_3: ", int(k_rtotal))
 
		#cuarto
		f_3 = int(input("Cuarto valor para ruffini: "))
 
		i_Terminada = int(f_3*g)
		i_total = int(i_rtotal+i_Terminada)
 
		print("Cociente_4: ", int(g))
		print("Resto_4: ", int(i_total))
		print("")
		print("Oprima una tecla para ir al menu...")
		msvcrt.getch()
 #opcion 5
	elif opcionMenu=="5":
		break
	else:
		print ("")