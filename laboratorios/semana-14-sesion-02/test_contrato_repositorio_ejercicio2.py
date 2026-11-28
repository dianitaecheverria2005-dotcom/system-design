
"""Ejercicio 2: las pruebas de contrato del repositorio.

El servicio se prueba rapido con RepositorioEnMemoria, un doble de prueba.
Eso solo vale si el doble se comporta igual que RepositorioSQLite. Estas
pruebas corren dos veces cada una, una con cada repositorio (la fixture
`repositorio` tiene dos parametros): si una pasa con uno y falla con el
otro, el doble miente.

    pytest test_contrato_repositorio_ejercicio2.py -v
"""

import sqlite3

import pytest

from dominio import semana_de
from repositorio import RepositorioEnMemoria, RepositorioSQLite


@pytest.fixture(params=["memoria", "sqlite"])
def repositorio(request, tmp_path):
    if request.param == "memoria":
        repo = RepositorioEnMemoria()
    else:
        repo = RepositorioSQLite(str(tmp_path / "reservau.db"))
    yield repo
    repo.cerrar()


def test_guardar_y_buscar(repositorio):
    repositorio.guardar("r1", "ana", "2026-11-17")
    assert repositorio.buscar("r1") == ("ana", "2026-11-17")


# TODO 1: buscar una reserva que no existe devuelve None.

def test_buscar_reserva_inexistente(repositorio):
    assert repositorio.buscar("r1") is None


# TODO 2: contar_en_semana cuenta solo las del estudiante en esa semana:
# guarda dos de ana en la semana del 16 de noviembre, una de ana en la del
# 23 y una de beto en la del 16, y comprueba los tres conteos.

def test_contar_en_semana(repositorio):
    repositorio.guardar("r1", "ana", "2026-11-16")
    repositorio.guardar("r2", "ana", "2026-11-17")
    repositorio.guardar("r3", "ana", "2026-11-23")
    repositorio.guardar("r4", "beto", "2026-11-18")

    semana1 = semana_de("2026-11-16")
    semana2 = semana_de("2026-11-23")

    assert repositorio.contar_en_semana("ana", semana1) == 2
    assert repositorio.contar_en_semana("ana", semana2) == 1
    assert repositorio.contar_en_semana("beto", semana1) == 1


# TODO 3: guardar dos veces el mismo id lanza sqlite3.IntegrityError
# (con pytest.raises).

def test_guardar_id_repetido(repositorio):
    repositorio.guardar("r1", "ana", "2026-11-17")

    with pytest.raises(sqlite3.IntegrityError):
        repositorio.guardar("r1", "beto", "2026-11-18")


# TODO 4: puntos_de suma todos los puntos del estudiante (0 si no tiene).

def test_sumar_puntos(repositorio):
    assert repositorio.puntos_de("ana") == 0

    repositorio.sumar_puntos("ana", 1)
    repositorio.sumar_puntos("ana", 2)
    repositorio.sumar_puntos("beto", 1)

    assert repositorio.puntos_de("ana") == 3
    assert repositorio.puntos_de("beto") == 1
    assert repositorio.puntos_de("pedro") == 0
