import time
from aeronave.sensores import obtener_datos_sensores
from aeronave.controles import calcular_ajustes, aplicar_ajustes

class Aeronave:
    def __init__(self):
        self.aeronave_en_vuelo = True
        self.intervalo_de_tiempo = 1
        self.alerones = 1.0
        self.timones = 0.5

    def ejecutar_ciclo(self):
        if self.aeronave_en_vuelo:
            giroscopio, acelerometro, velocidad = obtener_datos_sensores()
            ajustes = calcular_ajustes(giroscopio, acelerometro, velocidad)
            aplicar_ajustes(self.alerones, self.timones, ajustes=ajustes)
            self.esperar(self.intervalo_de_tiempo)
        else:
            print("La aeronave ha aterrizado.")

    def esperar(self, intervalo_de_tiempo):
        # Simulación: espera el intervalo de tiempo
        time.sleep(intervalo_de_tiempo)

    def aterrizar_aeronave(self):
        self.aeronave_en_vuelo = False
        print("Aeronave aterrizada.")

# Ejemplo de uso
aeronave = Aeronave()

# Bucle principal (simulación)
for _ in range(10):  # Repetir 10 veces (puedes ajustar según sea necesario)
    aeronave.ejecutar_ciclo()

# Aterrizar la aeronave al final
aeronave.aterrizar_aeronave()
