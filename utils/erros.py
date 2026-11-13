import functools
import logging
import psycopg
from psycopg import errors

logger = logging.getLogger(__name__)

class ErroDeNegocio(Exception):
    pass


class RegistroDuplicadoErro(ErroDeNegocio):
    pass


class RegistroRelacionadoErro(ErroDeNegocio):
    pass


class BancoIndisponivelErro(Exception):
    pass


class ErroDeBancoErro(Exception):
    pass


def tratar_erros_db(funcao):
    @functools.wraps(funcao)
    def wrapper(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)
        except errors.UniqueViolation as e:
            raise RegistroDuplicadoErro("Já existe um registro com esses dados.") from e
        
        except errors.ForeignKeyViolation as e:
            raise RegistroRelacionadoErro("Operação não permitida: o registro relacionado não existe ou está em uso.") from e
        
        except psycopg.OperationalError as e:
            logger.exception("Falha de conexão com o banco")
            raise BancoIndisponivelErro("Não foi possível acessar o banco de dados.") from e

        except psycopg.Error as e:
            logger.exception("Erro inesperado no banco")
            raise ErroDeBancoErro("Erro ao acessar o banco de dados.") from e
    return wrapper