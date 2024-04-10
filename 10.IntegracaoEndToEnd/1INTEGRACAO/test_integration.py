from app import *

def test_adicionar_verificar_quantidade():
    estoque = Estoque()
    
    produto1 = Produto("Mouse", 5)
    produto2 = Produto("Teclado", 10)
    
    estoque.adiciona_produto(produto=produto1)
    estoque.adiciona_produto(produto=produto2)
    
    assert estoque.verifica_quantidade("Mouse") == 5
    assert estoque.verifica_quantidade("Teclado") == 10
    
def test_adicionar_produto_existente():
    estoque = Estoque()
    
    produto1 = Produto("Mouse", 5)
    estoque.adiciona_produto(produto=produto1)
    
    produto2 = Produto("Mouse", 10)
    estoque.adiciona_produto(produto=produto2)
    
    assert estoque.verifica_quantidade("Mouse") == 15