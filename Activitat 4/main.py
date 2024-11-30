#Importem els atributs de les classes Cotxe i Colibri
from Cotxe import Cotxe
from Colibri import Colibri

#Instancia objecte Cotxe
cotxe_1 = Cotxe("Renault", "Scenic", "0345SFD", "Negre", 2020)

#Mostrem els 4 gettes de l'objecte Cotxe
print (f'La marca del meu cotxe és: {cotxe_1.getMarca()}')
print (f'El model del meu cotxe és: {cotxe_1.getModel()}')
print (f'La matricula del meu cotxe és: {cotxe_1.getMatricula()}')
print("")
print("Modifiquem la marca i la matricula i la mostrem per pantalla")

#Utilitzem set per modificar l'objecte
cotxe_1.setMarca("Hyundai")
cotxe_1.setMatricula("Lantra")
#Utilitzem get de nou per mostrar desprès del canvi
print(f'El meu nou cotxe és de la marca {cotxe_1.getMarca()}')
print(f'El model del meu nou cotxe és {cotxe_1.getMatricula()}')

print("")

#Instancia objecte Colibri
colibri_1 = Colibri("Pardo", "petit", "marró", "Patagonins", "America")

#Mostrem 4 getters del objecte Colibri
print (f'El nom del meu colibrí és: {colibri_1.getNom()}')
print (f'El tamany del meu colibrí és: {colibri_1.getTamany()}')
print (f'El color del meu colibrí és: {colibri_1.getColor()}')
print (f'La procedencia del meu colibrí: {colibri_1.getProcedencia()}')
print("")
print("Modifiquem el color i la procedencia i la mostrem per pantalla")

#Utilitzem set per modificar
colibri_1.setColor("morat")
colibri_1.setProcedencia("Asia")
#Utilitzem get de nou per mostrar desprès del canvi
print(f'El meu nou colibrí és ara de color: {colibri_1.getColor()}')
print(f'El meu nou colibrí és originari del següent continent: {colibri_1.getProcedencia()}')