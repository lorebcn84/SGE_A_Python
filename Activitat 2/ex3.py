""""En aquest exercici caldrà modificar la nota en número i mostrar-la en text. 
Es crearà una variable on es guardarà la nota numèrica i amb condicionals es mirarà 
la nota i segons la nota numèrica sortirà per pantalla la nota (S - suspès, A - aprovat, N - notable, E - excel·lent)"""

nota = float(input("Introdueix la nota: "))

if nota >= 0 and nota <= 4.99 :
    print("L'alumne ha suspès")
elif nota >= 5 and nota <= 6.5:
    print("L'alumne ha aprovat")
elif nota >= 6.6 and nota <= 8:
    print("L'alumne ha tret un notable")
elif nota >= 8.1 and nota <= 10:
    print("L'alumne ha tret un excel.lent!")
else:
    print("Nota incorrecta")