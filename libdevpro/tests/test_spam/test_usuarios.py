from libdevpro.spam.modelos import Usuario
from libdevpro.tests.test_spam.conftest import sessao


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Aruana')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Aruana'), Usuario(nome='Renzo')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

