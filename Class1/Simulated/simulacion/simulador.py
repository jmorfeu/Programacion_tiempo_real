# simulacion/simulador.py
from aeronave.aeronave import Aeronave
from utils.redis_publisher import publicar_evento


 
def iniciar_simulacion():
    aeronave = Aeronave()

    while aeronave.aeronave_en_vuelo:
        aeronave.ejecutar_ciclo()
        publicar_evento("Aeronave en vuelo")
    aeronave.aterrizar_aeronave()
