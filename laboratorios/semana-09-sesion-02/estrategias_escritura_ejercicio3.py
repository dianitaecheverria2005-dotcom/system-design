"""Ejercicio 3: dos estrategias de escritura, write-through para las
reservas y write-back para el contador de visitas.

Corre las pruebas con:

    pytest test_estrategias_escritura_ejercicio3.py

No cambies los nombres de las clases ni de los metodos: los tests
dependen de que existan exactamente asi.
"""


c
class DisponibilidadWriteThrough:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.cache = {}

    def disponibilidad(self, cancha, fecha):
        clave = (cancha, fecha)

        if clave not in self.cache:
            libres = self.repositorio.consultar_disponibilidad(cancha, fecha)
            self.cache[clave] = libres

        return self.cache[clave]

    def reservar(self, cancha, fecha, hora):
        libres = self.repositorio.consultar_disponibilidad(cancha, fecha)

        if hora not in libres:
            return False

        self.repositorio.registrar_reserva(cancha, fecha, hora)

        clave = (cancha, fecha)

        if clave in self.cache:
            self.cache[clave] = self.repositorio.consultar_disponibilidad(cancha, fecha)

        return True


class VisitasWriteBack:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.pendientes = {}

    def registrar_visita(self, cancha):
        if cancha not in self.pendientes:
            self.pendientes[cancha] = 0

        self.pendientes[cancha] += 1

    def visitas(self, cancha):
        guardadas = self.repositorio.consultar_visitas(cancha)

        if cancha in self.pendientes:
            return guardadas + self.pendientes[cancha]

        return guardadas

    def vaciar(self):
        for cancha in self.pendientes:
            cantidad = self.pendientes[cancha]
            self.repositorio.sumar_visitas(cancha, cantidad)

        self.pendientes = {}

    def caer(self):
        self.pendientes = {}
