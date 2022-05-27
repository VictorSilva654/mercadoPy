from utils.helper import formata_float_str_moeda

class Produto:

    contador = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo = Produto.contador
        self.__nome = nome
        self.__preco = preco
        Produto.contador += 1

    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def preco(self):
        return self.__preco

    def __str__(self):
        return f"Código: {self.codigo}\nNome: {self.nome}\nPreço: {self.preco}"

    
