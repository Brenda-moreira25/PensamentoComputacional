from .produto import produto

class tipoAlimenticio(produto):

        def __init__(self, nome: str, preco: float, laranja: str, berinjela: str, ):
                #tirar a duvida se crio uma lista? list.append[]
                super().__init__(nome, preco)
                self.__laranja = laranja
                self.__berinjela = berinjela
        
        def __str__(self):
                infos = super().__str__()
                infos +=  f"laranja: {self.__laranja}\n"
                infos +=  f"berinjela: {self.__berinjela}\n"
