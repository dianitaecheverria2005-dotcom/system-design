"""Ejercicio 3: la lista de espera con plazo para aceptar.

Avisar a beto no alcanza: si beto no contesta, la franja queda libre y
dani, que tambien esperaba, nunca se entera. La universidad pide esto:

ListaDeEsperaConPlazo es un observador de CalendarioConEventos (Ejercicio
2) que se suscribe a "liberada" y a "ocupada". Se construye con
ListaDeEsperaConPlazo(calendario, notificador, reloj, minutos_para_aceptar=15),
donde reloj es un RelojSimulado (reloj.py). Cada franja tiene su propia
fila de espera, y a lo sumo una oferta activa a la vez.

- anotar(estudiante, inicio, fin): pone al estudiante al final de la fila
  de esa franja (del dia del calendario). Si ya esta en esa fila, o ya
  tiene la oferta activa de esa franja: ValueError("ya esta en la lista").
  Si la franja esta libre en este momento: ValueError("la franja esta
  libre"), porque puede reservarla directamente.

- Cuando una franja se libera y no tiene oferta activa, se le ofrece al
  primero de su fila: sale de la fila, recibe "Tienes 15 minutos para
  aceptar cancha-1 2026-11-10 18-19" (con los minutos del constructor), y
  la oferta vence minutos_para_aceptar minutos despues de ahora. Si al
  primero no le alcanza el limite de horas (horas_de del calendario mas la
  duracion de la franja pasaria de MAXIMO_HORAS_POR_ESTUDIANTE), sale de
  la fila, recibe "No puedes tomar cancha-1 2026-11-10 18-19: pasarias el
  limite de horas", y la oferta pasa al siguiente. Si la fila queda vacia,
  no hay oferta.

- aceptar(estudiante, inicio, fin, id_reserva): si el estudiante no tiene
  la oferta activa de esa franja: ValueError("no tienes una oferta"). Si
  la oferta ya vencio (el reloj paso del minuto de vencimiento):
  ValueError("oferta vencida"), y la oferta sigue ahi hasta que alguien
  revise las vencidas. Si no, la oferta se cierra y se reserva la franja
  a su nombre con ese id.

- revisar_vencidas(): cada oferta vencida se cierra, su estudiante recibe
  "Vencio tu oferta de cancha-1 2026-11-10 18-19", y la franja se le
  ofrece al siguiente de la fila, con las mismas reglas. En la app en
  produccion esto lo corre un proceso cada minuto.

- Si alguien reserva directamente una franja que tiene una oferta activa
  (o una que se solapa con ella), la oferta se cierra y su estudiante
  recibe "La franja cancha-1 2026-11-10 18-19 ya no esta disponible". La
  fila de esa franja no cambia.

Los mensajes se envian con notificador.enviar(estudiante, texto), con el
texto exacto de arriba. Esta vez no hay codigo de partida: escribes la
clase completa. Corre las pruebas con:

    pytest test_ofertas_ejercicio3.py
"""


from eventos_ejercicio2 import ObservadorDeReservas
from reservas import MAXIMO_HORAS_POR_ESTUDIANTE, FranjaHoraria


class ListaDeEsperaConPlazo(ObservadorDeReservas):
    def __init__(self, calendario, notificador, reloj, minutos_para_aceptar=15):
        self.calendario = calendario
        self.notificador = notificador
        self.reloj = reloj
        self.minutos_para_aceptar = minutos_para_aceptar
        self.esperando = {}
        self.ofertas = {}

    def anotar(self, estudiante, inicio, fin):
        franja = FranjaHoraria(self.calendario.fecha, inicio, fin)

        if franja in self.esperando:
            if estudiante in self.esperando[franja]:
                raise ValueError("ya esta en la lista")

        if franja in self.ofertas:
            if self.ofertas[franja][0] == estudiante:
                raise ValueError("ya esta en la lista")

        if self.calendario.esta_libre(inicio, fin):
            raise ValueError("la franja esta libre")

        if franja not in self.esperando:
            self.esperando[franja] = []

        self.esperando[franja].append(estudiante)

    def ofrecer_siguiente(self, franja):
        if franja in self.ofertas:
            return

        if franja not in self.esperando:
            return

        if not self.calendario.esta_libre(franja.inicio, franja.fin):
            return

        while len(self.esperando[franja]) > 0:
            estudiante = self.esperando[franja].pop(0)
            horas = self.calendario.horas_de(estudiante)

            if horas + franja.duracion() > MAXIMO_HORAS_POR_ESTUDIANTE:
                texto = f"No puedes tomar {self.calendario.cancha} {franja.fecha} {franja.inicio}-{franja.fin}: pasarias el limite de horas"
                self.notificador.enviar(estudiante, texto)

            else:
                vencimiento = self.reloj.ahora() + self.minutos_para_aceptar
                self.ofertas[franja] = (estudiante, vencimiento)

                texto = f"Tienes {self.minutos_para_aceptar} minutos para aceptar {self.calendario.cancha} {franja.fecha} {franja.inicio}-{franja.fin}"
                self.notificador.enviar(estudiante, texto)

                return

    def al_liberarse(self, cancha, franja):
        for franja_esperada in self.esperando:
            if franja_esperada.se_solapa_con(franja):
                self.ofrecer_siguiente(franja_esperada)

    def aceptar(self, estudiante, inicio, fin, id_reserva):
        franja = FranjaHoraria(self.calendario.fecha, inicio, fin)

        if franja not in self.ofertas:
            raise ValueError("no tienes una oferta")

        persona, vencimiento = self.ofertas[franja]

        if persona != estudiante:
            raise ValueError("no tienes una oferta")

        if self.reloj.ahora() > vencimiento:
            raise ValueError("oferta vencida")

        del self.ofertas[franja]

        try:
            self.calendario.reservar(id_reserva, estudiante, inicio, fin)
        except ValueError:
            if self.calendario.esta_libre(inicio, fin):
                self.ofertas[franja] = (persona, vencimiento)
            raise

    def revisar_vencidas(self):
        for franja in list(self.ofertas):
            estudiante, vencimiento = self.ofertas[franja]

            if self.reloj.ahora() > vencimiento:
                del self.ofertas[franja]

                texto = f"Vencio tu oferta de {self.calendario.cancha} {franja.fecha} {franja.inicio}-{franja.fin}"
                self.notificador.enviar(estudiante, texto)

                self.ofrecer_siguiente(franja)

    def al_ocuparse(self, cancha, franja):
        for franja_oferta in list(self.ofertas):
            if franja_oferta.se_solapa_con(franja):
                estudiante = self.ofertas[franja_oferta][0]

                del self.ofertas[franja_oferta]

                texto = f"La franja {cancha} {franja_oferta.fecha} {franja_oferta.inicio}-{franja_oferta.fin} ya no esta disponible"
                self.notificador.enviar(estudiante, texto)
