import pytest
from  clasemaquina import Maquina

@pytest.fixture
def test_encender_maquina():
    maquina = Maquina("encendido", "apagado", "configuración predeterminada")
    assert maquina.encender_maquina() == "la maquina esta encendida."

def test_apagar_maquina():
    maquina = Maquina("encendido", "apagado", "configuración predeterminada")
    assert maquina.apagar_maquina() == "la maquina esta apagada."

def test_configuar_maquina():
    maquina = Maquina("encendido", "apagado", "configuración predeterminada")
    maquina.set_configurar("fichas personalizadas")
    assert maquina.get_configurar() == "fichas personalizadas"

def test_add_fichas():
    maquina = Maquina("encendido", "apagado", "configuración predeterminada")
    maquina.add_fichas(500)
    assert maquina.fichas_configuradas == 500
