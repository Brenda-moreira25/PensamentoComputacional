from .produto import produto

class tipoEletronico(produto):

        def __init__(self, nome: str, preco, celular: str, tablet: str ):
                #tirar a duvida se crio uma lista? list.append[]
                super().__init__(nome, preco)
                self.__celular = celular
                self.__tablet = tablet
        
        def __str__(self):
                infos = super().__str__()
                infos +=  f"celular: {self.__celular}\n"
                infos +=  f"tablet: {self.__tablet}\n"
