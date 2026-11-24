"""Ejercicio 3 (lo resuelves tu): el mismo patron de composicion que
viste en los patos, ahora sobre una jerarquia de vehiculos.

Corre las pruebas con:

    pytest test_vehiculo.py

No cambies las firmas de las clases ni los nombres de los metodos: los
tests dependen de que existan exactamente asi.
"""


class ComportamientoMover:
    def mover(self):
        raise NotImplementedError

class ConducirPorCarretera(ComportamientoMover):
    def mover(self):
        print("Conduciendo por carretera")


class NavegarPorAgua(ComportamientoMover):
    def mover(self):
        print("Navegando por agua.")


class Vehiculo:
    def __init__(self, comportamiento_mover):
        self.comportamiento_mover = comportamiento_mover

    def mover(self):
        return self.comportamiento_mover.mover()


class Auto(Vehiculo):
    def __init__(self):
        mueve_por_carretera = ConducirPorCarretera()
        super().__init__(mueve_por_carretera)

class Bote(Vehiculo):
    def __init__(self):
        mueve_por_agua = NavegarPorAgua()
        super().__init__(mueve_por_agua)


# TODO 5: la prueba de fuego del patron. Un avion no conduce ni navega:
# vuela. Crea tu propia clase de ComportamientoMover para esto (elige el
# nombre) y una clase Avion(Vehiculo) que la use, siguiendo exactamente
# el mismo patron que Auto y Bote de arriba.
#
# Ninguna de las clases que ya existen en este archivo (ComportamientoMover,
# ConducirPorCarretera, NavegarPorAgua, Vehiculo, Auto, Bote) debe cambiar
# una sola linea para que Avion funcione. Si tuviste que tocar alguna,
# algo en tu diseno todavia depende de herencia en vez de composicion.

class VuelaPorCielo(ComportamientoMover):
    def mover(self):
        print("Vuela por los cielos!")

class Avion(Vehiculo):
    def __init__(self):
        vuela_por_aire = VuelaPorCielo()
        super().__init__(vuela_por_aire)

if __name__ == "__main__":
    auto = Auto()
    bote = Bote()
    avion = Avion()

    auto.mover()
    bote.mover()
    avion.mover()