class Sensor():
    def __init__(self, id_indicador, tipo_sensor, emisor, receptor, estado, valor):
        self.id_indicador = id_indicador
        self.tipo_sensor = tipo_sensor #1 - Temperatura, 2 - Ultrasonido, 3 - Humedad valor = 0.0
        self.emisor = emisor # pin utilizado para el emisor
        self.receptor = receptor # pin  utilizado para el receptor
        self.estado = estado # 1 - Activo, 2 - Inactivo
        self.valor = valor # Valor del sensor
        self._estado_inicial = False
    def leer(self):
        print("Leyendo el sensor...")
    def apagar(self):
        self.estado = False
        print("Sensor apagado")
    def chequeo_incial(self):
        self._estado_inicial = True
        print("Verificacion de bateria")
class sensor_ultrasonico(Sensor):     
    def __init__(self, id_indicador, tipo_sensor, emisor, receptor, estado, valor, ubicacion):
        super().__init__(id_indicador, tipo_sensor, emisor, receptor, estado, valor)
        self.ubicacion = ubicacion





sensorA = Sensor(1, "Temperatura", 5, 6, True, 25)
sensorA.leer()
print("El id del sensor es: ", sensorA.id_indicador)

sensorB = Sensor(2, "Humedad", 7, 8, True, 60)
print("El id del sensor es: ", sensorB.id_indicador)

sensorB.chequeo_incial()
print("El estado_incial del sensor 8 es: ", sensorB._estado_inicial)

sensorC = sensor_ultrasonico(3,2,1,5,6,True,0)
sensorC.leer()
