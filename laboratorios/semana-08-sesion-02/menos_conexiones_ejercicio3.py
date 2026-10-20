"""Ejercicio 3: balanceador de menos conexiones (least connections).

Corre las pruebas con:

    pytest test_menos_conexiones_ejercicio3.py

Las pruebas tambien usan tu BalanceadorRoundRobin del Ejercicio 2, para
comparar los dos algoritmos con el mismo trafico.
"""


class BalanceadorMenosConexiones:
    def __init__(self, servidores):
        self.servidores = servidores

    def enviar(self, duracion):

        mejor_servidor = None

        for servidor in self.servidores:

            if servidor.health_check():

                if servidor.conexiones_activas() < servidor.capacidad:

                    if mejor_servidor is None:
                        mejor_servidor = servidor

                    elif servidor.conexiones_activas() < mejor_servidor.conexiones_activas():
                        mejor_servidor = servidor

        if mejor_servidor is not None:
            if mejor_servidor.atender(duracion):
                return mejor_servidor.nombre

        return None