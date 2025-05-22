from .CarrosCombustao import CarrosCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletr(CarrosCombustao):
    """ Classe que implementa métodos específicos de um carro convertido em eletrico"""

    def __init__(self, placa: str, modelo: str, marca: str,
                        ano: int, cor: str, valor_fipe: float,
                        combustivel: str, nPortas: int, nAssentos: int,
                        nCilindrada: int, nCambio: str, nivel_combustivel: int, 
                        nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        super().__init__(placa, modelo, marca,
                                ano, cor, valor_fipe, combustivel, nPortas, nAssentos,
                                nCilindrada, nCambio, nivel_combustivel)
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia 

    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"Nivel de bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos

    def abastecer(self, percentual: int) -> bool: #bool retorno boleano (verdadeiro ou falso)
            """Método abastecer desativado
            Argumento: percentual (int): percentual adicionado
            Retorno: bool: True se for possível abastecer, False se não
            """
            print("Carro convertido para elétrico, não é mais possível abastecer!")