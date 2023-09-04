from libdevpro.spam.enviador_de_email import Enviador
from libdevpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'aruanagarcia@gmai.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )