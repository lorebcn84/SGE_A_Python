'''Enunciat: 
Sumar números fins a arribar a 100 amb while. Caldrà sumar els números que estan inclosos entre 0 i 100. 
El programa deixarà d’executar-se quan s’arribi al número 100.
'''
num = 0
suma_nums = 0

while num <= 100:
    suma_nums += num
    num = num + 1

print(f"La suma de 0 a 100 és: {suma_nums}")