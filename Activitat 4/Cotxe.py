class Cotxe:
    def __init__(self, marca, model, matricula, color, any):
       self.marca = marca
       self.model = model
       self.matricula = matricula
       self.color = color
       self.any= any
       
    def getMarca(self):
        return self.marca
    def setMarca(self, new_marca):
        self.marca = new_marca
        
    def getModel(self):
        return self.model
    def setModel(self, new_model):
        self.model = new_model
        
    def getMatricula(self):
        return self.matricula
    def setMatricula(self, new_matricula):
        self.matricula = new_matricula
        
    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color
        
    def getAny(self):
        return self.any
    def setAny(self, new_any):
        self.any = new_any