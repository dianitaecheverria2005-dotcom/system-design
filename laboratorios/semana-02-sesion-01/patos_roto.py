"""Punto de partida: una jerarquia de herencia que se rompe.

Corre este archivo antes de la discusion de hoy:

    python patos_roto.py

Fijate bien en la ultima linea que se imprime. Esa es la pregunta que
abre la sesion: ¿por que un pato de goma "vuela"?
"""

class ComportamientoVuelo():
    def volar(self):
        raise NotImplementedError

class VuelaConAlas(ComportamientoVuelo):
    def volar(self):
        print("Volando con alas")

class NoVuela(ComportamientoVuelo):
    def volar(self):
        print("No vuela")

class ComportamientoGraznar:
    def graznar(self):
        raise NotImplementedError

class GraznidoNormal(ComportamientoGraznar):
    def graznar(self):
        print('Cuack!')

class GraznidoDeGoma(ComportamientoGraznar):
    def graznar(self):
        print('Chirrido de goma')

class Silencioso(ComportamientoGraznar):
    def graznar(self):
        print('...')

class Pato:
    def __init__(self, comportamiento_vuelo, comportamiento_graznido):
        self.comportamiento_vuelo = comportamiento_vuelo
        self.comportamiento_graznido = comportamiento_graznido

    def nadar(self):
        print("Nadando.")

    def graznar(self):
        self.comportamiento_graznido.graznar()

    def volar(self):
        self.comportamiento_vuelo.volar()

class PatoSalvaje(Pato):
    def __init__(self):
        vuela_alas = VuelaConAlas()
        granizo_normal = GraznidoNormal()
        super().__init__(vuela_alas, granizo_normal)


class PatoDeGoma(Pato):
    def __init__(self):
        no_vuela = NoVuela()
        granizo_de_goma = GraznidoDeGoma()
        super().__init__(no_vuela, granizo_de_goma)

class PatoDeCarton(Pato):
    def __init__(self):
        no_vuela = NoVuela()
        silencio = Silencioso()

        super().__init__(no_vuela, silencio)
        self.muerte = muerte

        def deshace_en_lluvia(self):
            self.muerte.deshace_en_lluvia()



if __name__ == "__main__":
    salvaje = PatoSalvaje()
    salvaje.nadar()
    salvaje.graznar()
    salvaje.volar()

    print()

    goma = PatoDeGoma()
    goma.nadar()
    goma.graznar()
    goma.volar()  # un pato de goma no vuela. ¿Por que este codigo lo permite?
