"""Pruebas del Ejercicio 2. La primera ya esta escrita. Escribe las demas
una a la vez, en este orden, y antes de cada una haz pasar la anterior:

1. Un estudiante sin reservas puede reservar.
2. Con 2 reservas en la semana, todavia puede.
3. Con 3 reservas en la semana, ya no puede.
4. Las reservas de otra semana no cuentan (2026-11-16 y 2026-11-23 son
   lunes de semanas distintas; 2026-11-22 es el domingo de la semana del 16).
5. Cancelar una reserva libera su lugar.
6. Un equipo oficial puede tener 6 reservas en la semana, pero no 7.
7. Registrar la cuarta reserva lanza ValueError (usa pytest.raises), y
   despues de intentarlo el estudiante sigue con 3.

Anota en la bitacora del README, por cada prueba: con que mensaje fallo,
que cambiaste para que pase, y que refactorizaste.
"""

import pytest
from cupos_ejercicio2 import CupoSemanal


def test_sin_reservas_puede_reservar():
    cupo = CupoSemanal()

    assert cupo.puede_reservar("ana", "2026-11-16")


def test_con_dos_reservas_puede_reservar():
    cupo = CupoSemanal()

    cupo.registrar("r1", "ana", "2026-11-16")
    cupo.registrar("r2", "ana", "2026-11-17")

    assert cupo.puede_reservar("ana", "2026-11-18")


def test_con_tres_reservas_no_puede_reservar():
    cupo = CupoSemanal()

    cupo.registrar("r1", "ana", "2026-11-16")
    cupo.registrar("r2", "ana", "2026-11-17")
    cupo.registrar("r3", "ana", "2026-11-18")

    assert not cupo.puede_reservar("ana", "2026-11-19")


def test_reservas_de_otra_semana_no_cuentan():
    cupo = CupoSemanal()

    cupo.registrar("r1", "ana", "2026-11-16")
    cupo.registrar("r2", "ana", "2026-11-17")
    cupo.registrar("r3", "ana", "2026-11-18")

    assert not cupo.puede_reservar("ana", "2026-11-22")
    assert cupo.puede_reservar("ana", "2026-11-23")


def test_cancelar_reserva_libera_cupo():
    cupo = CupoSemanal()

    cupo.registrar("r1", "ana", "2026-11-16")
    cupo.registrar("r2", "ana", "2026-11-17")
    cupo.registrar("r3", "ana", "2026-11-18")

    assert not cupo.puede_reservar("ana", "2026-11-19")

    cupo.cancelar("r1")

    assert cupo.puede_reservar("ana", "2026-11-19")


def test_equipo_oficial_tiene_cupo_de_seis():
    cupo = CupoSemanal()

    cupo.registrar_equipo_oficial("equipo1")

    for i in range(5):
        cupo.registrar("r" + str(i), "equipo1", "2026-11-16")

    assert cupo.puede_reservar("equipo1", "2026-11-16")

    cupo.registrar("r5", "equipo1", "2026-11-16")

    assert not cupo.puede_reservar("equipo1", "2026-11-16")

    with pytest.raises(ValueError, match="cupo semanal agotado"):
        cupo.registrar("r6", "equipo1", "2026-11-16")


def test_registrar_cuarta_reserva_lanza_error():
    cupo = CupoSemanal()

    cupo.registrar("r1", "ana", "2026-11-16")
    cupo.registrar("r2", "ana", "2026-11-17")
    cupo.registrar("r3", "ana", "2026-11-18")

    with pytest.raises(ValueError, match="cupo semanal agotado"):
        cupo.registrar("r4", "ana", "2026-11-19")

    assert not cupo.puede_reservar("ana", "2026-11-19")

    cupo.cancelar("r1")

    assert cupo.puede_reservar("ana", "2026-11-19")