from servidor import Servidor
from pico_ejercicio1 import simular_pico


def test_un_servidor_de_capacidad_100_rechaza_150_de_250():
    assert simular_pico(Servidor("unico", 100), 250, 5) == (100, 150)


def test_un_servidor_mas_grande_atiende_el_pico_completo():
    assert simular_pico(Servidor("grande", 300), 250, 5) == (250, 0)


def test_si_el_unico_servidor_cae_no_se_atiende_ninguna():
    grande = Servidor("grande", 300)
    grande.caer()
    assert simular_pico(grande, 250, 5) == (0, 250)

