
"""Ejercicio 1: la misma cobertura, en la base de la piramide. Empieza
vacio: se escribe en vivo.

Por cada prueba de punta a punta de test_suite_heredada.py que se pueda
bajar de nivel, una prueba unitaria del servicio (con RepositorioEnMemoria)
o una de integracion (con RepositorioSQLite o con la API), y una sola
prueba de punta a punta que recorra el camino completo.

    pytest test_rapidas_ejercicio1.py --durations=0
"""

import pytest
from repositorio import RepositorioEnMemoria, RepositorioSQLite
from servicio import ServicioDeReservas
from api import ApiDeReservas
from entorno_e2e import NavegadorSimulado


# Fixture

@pytest.fixture
def servicio():
    return ServicioDeReservas(repositorio=RepositorioEnMemoria())


# Pruebas unitarias

def test_la_cuarta_reserva_se_rechaza(servicio):
    servicio.reservar('r1', 'pedro', '2026-11-26')
    servicio.reservar('r2', 'pedro', '2026-11-27')
    servicio.reservar('r3', 'pedro', '2026-11-28')

    assert servicio.motivo_de_rechazo('pedro', '2026-11-30') is not None
    
#fixture: todos los componentes para que el ambiente de testing este funcionando

#unitarias

#integracion

def test_apli_cancelar_desconocida_404():
    repositorio_sql = RepositorioSQLite(':memory:')
    servicio_sql = ServicioDeReservas(repositorio=repositorio_sql)
    api = ApiDeReservas(servicio=servicio_sql)

    respuesta = api.manejar({
        'metodo': "DELETE",
        'ruta': '/reservas/reserva-inexistente',
        'cuerpo': {
            'minutos_de_anticipacion': 90
        }
    })

    assert respuesta['estado'] == 404

# E2E

def test_reservar_cancelar_ver_puntos():
    navegador = NavegadorSimulado()

    navegador.iniciar_sesion('pedro')

    assert navegador.reservar('r1', '2026-11-26')['estado'] == 201
    assert navegador.cancelar('r1', 30)['estado'] == 200
    assert navegador.ver_puntos() == 2