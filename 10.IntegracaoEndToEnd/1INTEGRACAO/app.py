class Produto:
    def __init__(self, nome, quantidade) -> None:
        self.nome = nome
        self.quantidade = quantidade
        
class Estoque:
    def __init__(self) -> None:
        self.produtos = {}

    def adiciona_produto(self, produto):
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade
    
    def verifica_quantidade(self, nome_produto):
        return self.produtos.get(nome_produto, 0)