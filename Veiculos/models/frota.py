class frota:
    """
    Classe criada para arquivar informações 
    """

#def __init__ utilizado para informar o que vai contar dentro dessa classe
    def __init__(self,veiculo):
         self.__frota = [veiculo]

    def adicionar(self, veiculo):
          self.__frota.append(veiculo)
         
    def calcular_consumo(self, distancia) -> float:
        consumo = 0
        for veiculo in self.__frota:
             consumo += veiculo.calcular_consumo(distancia)
        print(f"O consumo da frota foi {consumo} l")

