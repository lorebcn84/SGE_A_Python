class Colibri:
    def __init__(self, nom, tamany, color, tipus, procedencia):
       self.nom = nom
       self.tamany = tamany
       self.color = color
       self.tipus = tipus
       self.procedencia= procedencia
       
    def getNom(self):
        return self.nom
    def setNom(self, new_nom):
        self.nom = new_nom
        
    def getTamany(self):
        return self.tamany
    def setTamany(self, new_tamany):
        self.tamany = new_tamany
        
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color
        
    def getTipus(self):
        return self.tipus
    def setTipus(self, new_tipus):
        self.tipus = new_tipus
        
    def getProcedencia(self):
        return self.procedencia
    def setProcedencia(self, new_procedencia):
        self.procedencia = new_procedencia