import pytest

from libdevpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['aruanagarcia@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'tiadapadaria@gmail.com',
        'Nota fiscal',
        'Tia você precisa me enviar a nota fiscal.'
    )
    assert destinatario in resultado

