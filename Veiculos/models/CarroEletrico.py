from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    """ Classe que implementa métodos específicos de carros elétricos
    Argumento: Classe pai Veiculos
    """
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, valor_fipe: float, 
            nAssentos: int, nPortas: int, cor: str,
            nivel_bateria: int, tipo_bateria: str, autonomia: int):
        super().__init__(placa, modelo, marca, ano, cor, valor_fipe) #Atributos herdados da classe pai Veiculos.
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia 

    def __str__(self):
        """Retorna uma string com as informações do veiculo"""
        infos = super().__str__()
        infos =  f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Nivel de bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos