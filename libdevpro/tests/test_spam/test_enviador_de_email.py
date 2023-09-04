import pytest

from libdevpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'aruanagarcia@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'renzo@gmail.com',
        'Cursos Python pro.',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'aruanagarcia']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'renzo@gmail.com',
            'Cursos Python pro.',
            'Primeira turma Guido Von Rossum aberta.'
        )

