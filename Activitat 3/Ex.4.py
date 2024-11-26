'''Imprimir els números parells i els imparells continguts en la següent llista. 
Utilitzar for: num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
'''
numeros = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

pars = ""
impars = ""

for numero in numeros:
    if numero % 2 == 0: 
        pars += str(numero) + " "
    else:            
        impars += str(numero) + " "

print("Parells:", pars)
print("Imparells:", impars)


