import pytest

from libdevpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['aruanagarcia@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'tiadapadaria@gmail.com',
        'Nota fiscal',
        'Tia você precisa me enviar a nota fiscal.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'tiadapadaria@gmail.com',
            'Nota fiscal',
            'Tia você precisa me enviar a nota fiscal.'
    )
    



