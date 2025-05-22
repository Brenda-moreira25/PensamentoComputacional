from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletr import CarroConvEletr
from models.caminhao import caminhao
from models.carro import carro
from models.moto import moto


#voyage = Veiculos("BCE9D36", "Voyage",  "Volkswagen", 2018,    "Vermelho", 47793) #Classe: Veiculos

#jetta_gli = CarrosCombustao("JDM9D36", "Jetta GLI",  "Volkswagen", 2025, "Vermelho", 250000, "Gasolina", 
#                            4, 5, 2000, "AT 7", 24) #Classe: CarroCombustao

#tesla_model = CarroEletrico("IJI8K0T","Tesla model 5","Tesla", 2025, 500000, 5, 4, "Branco",
#                            65,"Lítio", 491) #Classe: CarroEletrico

#fusca_eletrico = CarroConvEletr(placa = "IAA0D40", modelo = "Fusca 1600 Elétrico", marca = "Volkswagem",
#                                ano  = 1975, cor = "Azul", combustivel  = "Gasolina", 
#                                nPortas = 4, nAssentos = 5, nCilindrada = 1600,nCambio = "MT 4", 
#                                nivel_combustivel = 24, nivel_bateria = 65, tipo_bateria ="Litio", valor_fipe = 25000,
#                               autonomia  = 150 ) #Classe: CarroConvEletr


Pepsi = caminhao(placa = "ila9880", modelo = "ford", marca = "BM",
                       ano = 2000 , cor = "BRANCO", eficiencia_media = 5 , km_litros = 5, valor_fipe = 20000 ) #Classe: caminhao

palio2010 = carro(placa = "MGY1866", modelo = "FIRE", marca = "FIAT",
                       ano = 2010, cor = "VERMELHO", valor_fipe = 22000, eficiencia_media = 12, km_litros = 12) #Classe: carro

biz = moto(placa = "XXZ5610", modelo = "FASER", marca = "HONDA",
                       ano = 2015, cor = "PRETA", eficiencia_media = 20, 
                       km_litros = 20, valor_fipe = 25000)#Classe: CarroConvEletr



# print(jetta_gli)
# if jetta_gli.abastecer(10):
#     print("Abastecido com sucesso!")
# else:
#     print("Erro ao abastecer")

# print(jetta_gli)
# print(fusca_eletrico)


distancia = float(input("Qual a distancia a ser percorrida?"))

veiculo = input("Qual o veículo a ser utilizado?")

if veiculo == "moto":
      biz.calcular_consumo(distancia)
      print(biz)
      
elif veiculo == "caminhao":
      caminhao.calcular_consumo(distancia)
      print(Pepsi)

else:
      veiculo == "carro"
      carro.calcular_consumo(distancia)
      print(palio2010)











