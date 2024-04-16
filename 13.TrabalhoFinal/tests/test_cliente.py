import pytest
import sys
sys.path.append("recursos")
from database_manager import *

@pytest.fixture(scope="session")
def connection():
    manager = DatabaseManager("users.db")
    yield manager
    manager.conn.close()

@pytest.mark.parametrize("nome", ["bruno", "paula"])
@pytest.mark.parametrize("email", ["nãosei@yaho.cm", "naoemail@some.moon"])
@pytest.mark.parametrize("telefone", [ "182730952", "00000000"])
@pytest.mark.parametrize("endereco", ["rua talvez","avenida nome de rua"])
@pytest.mark.parametrize("cidade", ["soroca", "sao paulo"])
@pytest.mark.parametrize("estado", ["mminas", "saopaulo"])
@pytest.mark.parametrize("cep", ["13084536", "18945123", "0800734131"])
@pytest.mark.parametrize("datacadastro", ["1999-06-02", "2000-09-30", "1993-08-13"])
@pytest.mark.parametrize("datanascimento", ["1999-06-02", "2000-09-30", "1993-08-13"])
def test_incluir_cliente_should_return_true(connection,
                         nome,
                         email,
                         telefone,
                         endereco,
                         cidade,
                         estado,
                         cep,
                         datacadastro,
                         datanascimento):
    assert connection.conn is not None
    cliente = Cliente(nome, email, telefone, endereco, cidade, estado, cep, datacadastro, datanascimento)
    assert connection.incluir_cliente(cliente)

@pytest.mark.parametrize("nome", ["bruno", "paula"])
@pytest.mark.parametrize("email", ["bla@gmailcom", "nãoseiyaho.cm", "naoemailsomemoon", "@.@ @.", "@.", "@@@@@@@@......."])
@pytest.mark.parametrize("telefone", ["182730951"])
@pytest.mark.parametrize("endereco", ["rua naosei"])
@pytest.mark.parametrize("cidade", ["campinas"])
@pytest.mark.parametrize("estado", ["planetaterra"])
@pytest.mark.parametrize("cep", ["13084536"])
@pytest.mark.parametrize("datacadastro", ["1999-06-02"])
@pytest.mark.parametrize("datanascimento", ["1999-06-02"])
def test_incluir_cliente_invalid_emails_should_return_false(connection,
                         nome,
                         email,
                         telefone,
                         endereco,
                         cidade,
                         estado,
                         cep,
                         datacadastro,
                         datanascimento):
    assert connection.conn is not None
    cliente = Cliente(nome, email, telefone, endereco, cidade, estado, cep, datacadastro, datanascimento)
    assert connection.incluir_cliente(cliente) is not True

@pytest.mark.parametrize("nome", ["antonio", "paula"])
@pytest.mark.parametrize("email", ["nãosei@yaho.cm", "naoemail@some.moon"])
@pytest.mark.parametrize("telefone", ["182730952", "00000000"])
@pytest.mark.parametrize("endereco", ["rua talvez","avenida nome de rua"])
@pytest.mark.parametrize("cidade", ["soroca", "sao paulo"])
@pytest.mark.parametrize("estado", ["mminas", "saopaulo"])
@pytest.mark.parametrize("cep", ["18945123", "0800734131"])
@pytest.mark.parametrize("datacadastro", ["1999.06.02", "2000*09*30", "1993-13-08", "1993-03-8", "1993-13-08", "08-13-1999"])
@pytest.mark.parametrize("datanascimento", ["2000-09-30", "1993-08-13"])
def test_incluir_cliente_invalid_date_should_return_false(connection,
                         nome,
                         email,
                         telefone,
                         endereco,
                         cidade,
                         estado,
                         cep,
                         datacadastro,
                         datanascimento):
    assert connection.conn is not None
    cliente = Cliente(nome, email, telefone, endereco, cidade, estado, cep, datacadastro, datanascimento)
    assert connection.incluir_cliente(cliente) is not True


@pytest.mark.parametrize("id", [i for i in range(1, 3)])
def test_cliente_existe_should_return_true(connection,id):
    assert connection.conn is not None
    cliente = connection.verificar_cliente(id)
    assert cliente is not "Erro ao buscar o cliente."

@pytest.mark.parametrize("id", [i for i in range(1, 3)])
@pytest.mark.parametrize("campo", ["nome", "cidade", "endereco"])
@pytest.mark.parametrize("valor", ["bruno", "campinas", "rua paula bueno"])
def test_atualizar_cliente_should_return_true(connection, id, campo, valor):
    assert connection.conn is not None
    cliente = connection.atualizar_cliente(id, campo, valor)
    assert cliente is not "Erro ao buscar o cliente."
