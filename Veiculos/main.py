from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletr import CarroConvEletr
from models.caminhao import caminhao
from models.carro import carro
from models.moto import moto


def main():
      # Criando instâncias de veículos
      veiculo1 = CarrosCombustao("ABC1234", "Fusca", 15.0, 50.0, "Gasolina")
      veiculo2 = CarroEletrico("XYZ5678", "Tesla Model S", 0.2, 100.0, 75.0)
      veiculo3 = CarroConvEletr("LMN9101", "Toyota Prius", 20.0, 45.0, "Híbrido")
      veiculo4 = caminhao("QRS2345", "Volvo FH", 8.0, 300.0, 10000)
      veiculo5 = carro("TUV6789", "Civic", 12.0, 40.0, "Gasolina")
      veiculo6 = moto("WXY3456", "Honda CB500F", 25.0, 15.0)
      
      # Adicionando veículos a uma lista
      lista_veiculos = [veiculo1, veiculo2, veiculo3, veiculo4, veiculo5, veiculo6]
      
      # Exibindo informações dos veículos
      for veiculo in lista_veiculos:
            print(veiculo)
           
if __name__ == "__main__":
    main()  










