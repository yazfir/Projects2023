class Avion:

    def __init__(self, modelo, numMotores, lstPasajeros ):
        self.modelo = modelo
        self.numMotores  = numMotores
        self.lstPasajeros = lstPasajeros
        
    def muestraModeloyMotor(self):
        print("Modelo:", self.modelo,"Núm. Motores:", self.numMotores)

    def muestraListaPasajeros(self):
        for x in self.lstPasajeros:
            print("Pasajero:",x)

avion1 = Avion('Modelo1',4,['Ana','Pedro','Pablo'])
avion1.muestraModeloyMotor()
avion1.muestraListaPasajeros()