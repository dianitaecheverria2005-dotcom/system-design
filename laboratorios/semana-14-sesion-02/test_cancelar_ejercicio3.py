
"""Ejercicio 3: las pruebas de cancelar. Sin pruebas de partida: las
escribes tu, decidiendo de que tipo es cada una.

    pytest test_cancelar_ejercicio3.py --durations=0
"""

import pytest
from repositorio import RepositorioEnMemoria, RepositorioSQLite
from servicio import ServicioDeReservas


# Fixture

@pytest.fixture
def servicio():
    return ServicioDeReservas(repositorio=RepositorioEnMemoria())


# Pruebas unitarias

def test_cancelar_elimina_reserva(servicio):
    servicio.reservar("r1", "pedro", "2026-11-26")
    servicio.cancelar("r1", 3000)

    assert servicio.repositorio.buscar("r1") is None


def test_cancelar_tarde_suma_dos_puntos(servicio):
    servicio.reservar("r1", "pedro", "2026-11-26")
    servicio.cancelar("r1", 30)

    assert servicio.repositorio.puntos_de("pedro") == 2


def test_cancelar_suma_un_punto(servicio):
    servicio.reservar("r1", "pedro", "2026-11-26")
    servicio.cancelar("r1", 600)

    assert servicio.repositorio.puntos_de("pedro") == 1


def test_cancelar_con_tiempo_no_suma_puntos(servicio):
    servicio.reservar("r1", "pedro", "2026-11-26")
    servicio.cancelar("r1", 3000)

    assert servicio.repositorio.puntos_de("pedro") == 0


def test_cancelar_reserva_desconocida(servicio):
    with pytest.raises(ValueError, match="reserva desconocida"):
        servicio.cancelar("r1", 90)


def test_cancelar_no_elimina_otras_reservas(servicio):
    servicio.reservar("r1", "pedro", "2026-11-26")
    servicio.reservar("r2", "pedro", "2026-11-27")

    servicio.cancelar("r1", 3000)

    assert servicio.repositorio.buscar("r1") is None
    assert servicio.repositorio.buscar("r2") == ("pedro", "2026-11-27")


# Integracion

def test_cancelar_sqlite_no_elimina_otras_reservas():
    repositorio_sql = RepositorioSQLite(":memory:")
    servicio_sql = ServicioDeReservas(repositorio=repositorio_sql)

    servicio_sql.reservar("r1", "pedro", "2026-11-26")
    servicio_sql.reservar("r2", "pedro", "2026-11-27")

    servicio_sql.cancelar("r1", 30)

    assert repositorio_sql.buscar("r1") is None
    assert repositorio_sql.buscar("r2") == ("pedro", "2026-11-27")
    assert repositorio_sql.puntos_de("pedro") == 2

    repositorio_sql.cerrar()


def test_cancelar_sqlite_libera_un_solo_cupo():
    repositorio_sql = RepositorioSQLite(":memory:")
    servicio_sql = ServicioDeReservas(repositorio=repositorio_sql)

    servicio_sql.reservar("r1", "pedro", "2026-11-26")
    servicio_sql.reservar("r2", "pedro", "2026-11-27")
    servicio_sql.reservar("r3", "pedro", "2026-11-28")

    servicio_sql.cancelar("r1", 3000)

    servicio_sql.reservar("r4", "pedro", "2026-11-29")

    assert servicio_sql.motivo_de_rechazo("pedro", "2026-11-29") == "cupo semanal agotado"

    repositorio_sql.cerrar()
