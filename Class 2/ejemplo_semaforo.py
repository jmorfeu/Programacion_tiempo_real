import threading
import time

# Declaración e inicialización de variables globales y tipos
shared_variable = 0
sval = 1
semaphore = threading.Semaphore(value=sval)

# Función para la hebra A
def hebra_A():
    global shared_variable

    # Ejecutar código hasta el punto P1
    print("Hebra A ejecutando hasta P1")

    # Bloquear la ejecución mediante sem_wait
    semaphore.acquire()
    print("Hebra A bloqueada en sem_wait")

    # Continuar la ejecución después de recibir la señal
    print("Hebra A reanudada después de sem_post")
    shared_variable += 1

# Función para la hebra B
def hebra_B():
    global shared_variable

    # Ejecutar código hasta el punto P2
    print("Hebra B ejecutando hasta P2")

    # Enviar una señal al semáforo mediante sem_post
    semaphore.release()
    print("Hebra B enviando señal con sem_post")

    # Continuar la ejecución después de enviar la señal
    print("Hebra B reanudada después de sem_post")
    shared_variable -= 1

# Hebra principal
if __name__ == "__main__":
    # Creación de las hebras A y B
    thread_A = threading.Thread(target=hebra_A)
    thread_B = threading.Thread(target=hebra_B)

    # Iniciar las hebras
    thread_A.start()
    thread_B.start()

    # Esperar a que ambas hebras terminen
    thread_A.join()
    thread_B.join()

    # Continuar con el código de la hebra principal después de la finalización de las hebras
    print("Hebra principal continuando...")
