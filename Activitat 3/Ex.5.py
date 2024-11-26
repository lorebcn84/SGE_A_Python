'''Enunciat:
Copiar exercici anterior i modificar-lo per a que mostri la suma dels números parells i la suma dels números imparells.
'''
numeros = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

suma_pars = 0
suma_impars = 0

for numero in numeros:
    if numero % 2 == 0: 
        suma_pars += numero
    else:             
        suma_impars += numero

print(f"Suma Parells: {suma_pars}")
print(f"Suma Imparells: {suma_impars}")