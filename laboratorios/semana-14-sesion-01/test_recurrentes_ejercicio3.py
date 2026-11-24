import pytest
from recurrentes_ejercicio3 import AgendaDeCancha
from reservas import CalendarioDeCancha


def test_crear_calendario():
    agenda = AgendaDeCancha("Cancha 1")
    calendario = agenda.calendario("2026-11-16")

    assert isinstance(calendario, CalendarioDeCancha)


def test_misma_fecha_mismo_calendario():
    agenda = AgendaDeCancha("Cancha 1")

    calendario1 = agenda.calendario("2026-11-16")
    calendario2 = agenda.calendario("2026-11-16")

    assert calendario1 is calendario2


def test_fechas_distintas_calendarios_distintos():
    agenda = AgendaDeCancha("Cancha 1")

    calendario1 = agenda.calendario("2026-11-16")
    calendario2 = agenda.calendario("2026-11-23")

    assert calendario1 is not calendario2


def test_reservar_una_semana():
    agenda = AgendaDeCancha("Cancha 1")

    resultado = agenda.reservar_cada_semana(
        "entreno", "ana", "2026-11-16", 8, 10, 1
    )

    assert resultado == [
        ("2026-11-16", "reservada")
    ]

    assert not agenda.calendario("2026-11-16").esta_libre(8, 10)


def test_reservar_tres_semanas():
    agenda = AgendaDeCancha("Cancha 1")

    resultado = agenda.reservar_cada_semana(
        "entreno", "ana", "2026-11-16", 8, 10, 3
    )

    assert resultado == [
        ("2026-11-16", "reservada"),
        ("2026-11-23", "reservada"),
        ("2026-11-30", "reservada")
    ]


def test_franja_ocupada_no_impide_otras_reservas():
    agenda = AgendaDeCancha("Cancha 1")

    agenda.calendario("2026-11-23").reservar(
        "reserva1", "pedro", 8, 10
    )

    resultado = agenda.reservar_cada_semana(
        "entreno", "ana", "2026-11-16", 8, 10, 3
    )

    assert resultado == [
        ("2026-11-16", "reservada"),
        ("2026-11-23", "ocupada"),
        ("2026-11-30", "reservada")
    ]

    assert len(agenda.calendario("2026-11-23").reservas()) == 1


def test_limite_de_horas():
    agenda = AgendaDeCancha("Cancha 1")

    agenda.calendario("2026-11-23").reservar(
        "reserva1", "ana", 10, 12
    )

    resultado = agenda.reservar_cada_semana(
        "entreno", "ana", "2026-11-16", 8, 10, 3
    )

    assert resultado == [
        ("2026-11-16", "reservada"),
        ("2026-11-23", "limite"),
        ("2026-11-30", "reservada")
    ]

    assert agenda.calendario("2026-11-23").horas_de("ana") == 2


def test_cero_semanas_lanza_error():
    agenda = AgendaDeCancha("Cancha 1")

    with pytest.raises(ValueError):
        agenda.reservar_cada_semana(
            "entreno", "ana", "2026-11-16", 8, 10, 0
        )


def test_trece_semanas_lanza_error():
    agenda = AgendaDeCancha("Cancha 1")

    with pytest.raises(ValueError):
        agenda.reservar_cada_semana(
            "entreno", "ana", "2026-11-16", 8, 10, 13
        )


def test_semanas_invalidas_no_registran_reservas():
    agenda = AgendaDeCancha("Cancha 1")

    with pytest.raises(ValueError):
        agenda.reservar_cada_semana(
            "entreno", "ana", "2026-11-16", 8, 10, 13
        )

    assert agenda.calendario("2026-11-16").reservas() == []
    assert agenda.calendario("2026-11-23").reservas() == []


def test_reservar_doce_semanas():
    agenda = AgendaDeCancha("Cancha 1")

    resultado = agenda.reservar_cada_semana(
        "entreno", "ana", "2026-11-16", 8, 10, 12
    )

    assert len(resultado) == 12

    for fecha, estado in resultado:
        assert estado == "reservada"


def test_identificadores_consecutivos():
    agenda = AgendaDeCancha("Cancha 1")

    agenda.reservar_cada_semana(
        "entreno", "ana", "2026-11-16", 8, 10, 3
    )

    assert agenda.calendario("2026-11-16").reservas()[0][0] == "entreno-1"
    assert agenda.calendario("2026-11-23").reservas()[0][0] == "entreno-2"
    assert agenda.calendario("2026-11-30").reservas()[0][0] == "entreno-3"