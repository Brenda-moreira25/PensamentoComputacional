from .Veiculos import Veiculos

class moto(Veiculos):
    """ Método que irá adicionar informações da classe caminhao

    Argumento: Classe pai Veiculos
    """

    #Init são todos os atributos que serão informados/utilizados
    def __init__(self, placa: str, modelo: str, marca: str,
                       ano: int, cor: str, eficiencia_media: int, 
                       km_litros: int, valor_fipe: int) -> None:
            
        #Será os atriutos que viram da classe mãe
        super().__init__(placa, modelo, marca,
                       ano, cor, valor_fipe)
        self.__eficiencia_media = eficiencia_media
        self.__km_litros = km_litros

    """Retorna uma string com as informações do veiculo"""
    def __str__(self) -> str:       
        infos =  super().__str__()
        infos += f"eficiencia_media: {self.__eficiencia_media}\n"
        infos += f"km_litros: {self.__km_litros}\n"
        return infos

    def calcular_consumo(self, distancia) -> float:
        consumo = distancia/20
        print(f"O consumo utilizado pelo moto será {consumo}")
