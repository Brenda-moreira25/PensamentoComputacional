from .produto import produto

class tipoAlimenticio:

        def __init__(self, verdura, fruta, mistura, laranja: str, berinjela: str, ):
                #tirar a duvida se crio uma lista? list.append[]
                super().__init__(self, verdura, fruta, mistura, tipoAlimenticio)
                self.__laranja = laranja
                self.__berinjela = berinjela
        
        def __str__(self):
                infos = super().__str__()
                infos +=  f"laranja: {self.__laranja}\n"
                infos +=  f"berinjela: {self.__berinjela}\n"
