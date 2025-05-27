from .produto import produto

class tipoEletronico:

        def __init__(self, celular: str, tablet: str ):
                #tirar a duvida se crio uma lista? list.append[]
                super().__init__(self,)
                self.__celular = celular
                self.__tablet = tablet
        
        def __str__(self, celular: str, tablet: str):
                infos = super().__str__(tv, radio) -> str
                infos +=  f"celular: {self.__celular}\n"
                infos +=  f"tablet: {self.__tablet}\n"
