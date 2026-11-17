"""Ejercicio 3: la cancha que se divide en dos.

La cancha-3 del complejo se puede reservar completa o por mitades: una
red la divide en la media cancha "cancha-3-a" y la "cancha-3-b". Es a la
vez algo que se reserva (la cancha completa) y algo que contiene otras
cosas que se reservan (sus mitades).

Escribe CanchaDivisible, un Recurso de inventario_ejercicio2.py (por eso
este ejercicio necesita ese archivo completo):

- CanchaDivisible(nombre) crea sus dos mitades, Reservable(nombre + "-a",
  "media cancha") y Reservable(nombre + "-b", "media cancha"), en ese
  orden. La cancha completa es de tipo "cancha" y no tiene calendario
  propio: esta libre en una franja si y solo si sus dos mitades lo estan.

- buscar(tipo, inicio, fin): para "cancha", [nombre] si la cancha
  completa esta libre, o []. Para "media cancha", los nombres de las
  mitades libres. Para cualquier otro tipo, [].

- contar(tipo): 1 para "cancha", 2 para "media cancha", 0 para otro.

- encontrar(nombre): la propia cancha si el nombre es el suyo, la mitad
  si es el de una mitad, o None.

- rutas(tipo, inicio, fin, ruta): para "cancha", [ruta + nombre] en los
  mismos casos que buscar; para "media cancha", cada mitad libre como
  ruta + nombre + " / " + nombre de la mitad.

- reservar(id_reserva, estudiante, inicio, fin): reserva la cancha
  completa, es decir, las dos mitades, con los ids id_reserva + "-a" e
  id_reserva + "-b". Si alguna mitad no esta libre: ValueError("franja
  ocupada"). Si en alguna mitad el estudiante pasaria de
  MAXIMO_HORAS_POR_ESTUDIANTE: ValueError("limite de horas alcanzado"),
  verificado despues de la ocupacion. En los dos casos, ninguna mitad
  cambia.

Una mitad se reserva como cualquier Reservable: reservar_en(campus,
"cancha-3-a", ...) la encuentra y la reserva sola.

Esta vez no hay codigo de partida. Corre las pruebas con:

    pytest test_cancha_divisible_ejercicio3.py
"""


from inventario_ejercicio2 import Recurso, Reservable
from reservas import MAXIMO_HORAS_POR_ESTUDIANTE


class CanchaDivisible(Recurso):
    def __init__(self, nombre):
        super().__init__(nombre)

        self.mitad_a = Reservable(nombre + "-a", "media cancha")
        self.mitad_b = Reservable(nombre + "-b", "media cancha")

        self.hijos = [self.mitad_a, self.mitad_b]

    def buscar(self, tipo, inicio, fin):
        if tipo == "cancha":
            for mitad in self.hijos:
                if not mitad.calendario.esta_libre(inicio, fin):
                    return []
            return [self.nombre]

        if tipo == "media cancha":
            encontrados = []
            for mitad in self.hijos:
                encontrados += mitad.buscar(tipo, inicio, fin)
            return encontrados

        return []

    def contar(self, tipo):
        if tipo == "cancha":
            return 1

        if tipo == "media cancha":
            return 2

        return 0

    def encontrar(self, nombre):
        if self.nombre == nombre:
            return self

        for mitad in self.hijos:
            if mitad.nombre == nombre:
                return mitad

        return None

    def rutas(self, tipo, inicio, fin, ruta):
        if tipo == "cancha":
            if self.buscar(tipo, inicio, fin):
                return [ruta + self.nombre]
            return []

        if tipo == "media cancha":
            encontrados = []

            for mitad in self.hijos:
                encontrados += mitad.rutas(
                    tipo, inicio, fin,
                    ruta + self.nombre + " / "
                )

            return encontrados

        return []

    def reservar(self, id_reserva, estudiante, inicio, fin):
        for mitad in self.hijos:
            if not mitad.calendario.esta_libre(inicio, fin):
                raise ValueError("franja ocupada")

        duracion = fin - inicio

        for mitad in self.hijos:
            horas = mitad.calendario.horas_de(estudiante)

            if horas + duracion > MAXIMO_HORAS_POR_ESTUDIANTE:
                raise ValueError("limite de horas alcanzado")

        for mitad, sufijo in [
            (self.mitad_a, "-a"),
            (self.mitad_b, "-b")
        ]:
            for reserva in mitad.calendario.reservas():
                if reserva[0] == id_reserva + sufijo:
                    raise ValueError("id repetido")

        self.mitad_a.reservar(
            id_reserva + "-a", estudiante, inicio, fin
        )

        self.mitad_b.reservar(
            id_reserva + "-b", estudiante, inicio, fin
        )
