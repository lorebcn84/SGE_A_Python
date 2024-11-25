"""Aplicar IVA segons el salari
En aquest exercici, s’aplicarà un IVA (0, 10, 21) segons el salari que s’indiqui.
Crear una variable de nom salari. Si el salari és menor de 15.000, s’aplica un 0% d’IVA. 
Si el salari és menor de 30.000 s’aplica un 10% de l’iva. Si el salari és menor a 60.000 s’aplica un IVA del 21%.
"""
salari = int(input("Introdueix el teu salari per calcular el tipus d'IVA: "))

if salari >= 0 and salari < 15000:
    print(f"No s'aplica cap tipus d'IVA, cobrarás {salari}€")
elif salari >= 15000 and salari < 30000:
    impost = salari * 0.10
    total_salari = salari - impost
    print(f"S'aplicarà {impost}€ d'IVA i cobraràs en total {total_salari}€")
elif salari >= 30000 and salari < 60000:
    impost = salari * 0.21
    total_salari = salari - impost
    print(f"S'aplicarà {impost}€ d'IVA i cobraràs en total {total_salari}€")
else:
    print("Import incorrecte")