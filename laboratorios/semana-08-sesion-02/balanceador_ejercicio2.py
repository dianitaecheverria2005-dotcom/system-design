"""Ejercicio 2: balanceador round robin con health check.

Corre las pruebas con:

    pytest test_balanceador_ejercicio2.py

No cambies los nombres de la clase ni de los metodos: los tests
dependen de que existan exactamente asi.
"""

class BalanceadorRoundRobin:
    def __init__(self, servidores):
        self.servidores = servidores
        self.siguiente = 0

    def enviar(self, duracion):

        cantidad = len(self.servidores)

        for i in range(cantidad):

            posicion = (self.siguiente + i) % cantidad

            servidor = self.servidores[posicion]

            if servidor.health_check():

                if servidor.atender(duracion):

                    self.siguiente = (posicion + 1) % cantidad

                    return servidor.nombre

        return None