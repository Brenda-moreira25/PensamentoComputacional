from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """
    Classe que representa um carro de combustão, herda de Veiculos
    """
    
    def __init__(self, placa: str, modelo: str, marca: str,
                       ano: int, cor: str, valor_fipe: float,
                       combustivel: str, nPortas: int, nAssentos: int,
                       nCilindrada: int, nCambio: str, nivel_combustivel: int) -> None:
        super().__init__(placa, modelo, marca,
                               ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel

        
    def __str__(self) -> str:
        """
        Retorna uma string com as informações do carro de combustão
        """
        # Reutiliza o método __str__ da classe pai (Veiculos)
        infos = super().__str__()
        # Adiciona as informações especificas do carro a combustão
        infos += f"Combustivel: {self.__combustivel}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"Número de cilindrada: {self.__nCilindrada}\n"
        infos += f"Câmbio: {self.__nCambio}\n"
        infos += f"Nível Combustível: {self.__nivel_combustivel}"
        return infos
    
    def abastecer(self, percentual: int) -> bool: #bool retorno boleano (verdadeiro ou falso)
        """ Método para abastecer um carro a combustão
        Argumento: percentual (int): percentual adicionado
        Retorno: bool: True se for possível abastecer, False se não
        """
        novo_percentual = self.__nivel_combustivel + percentual #Abastecendo
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True

