class DistanciaNegeativa(Exception):
    pass

try:
    distancia = float(input("Digite a distancia: "))
    if distancia < 0:
            raise DistanciaNegeativa("Digite a distancia: ")
except ValueError as erro:
     print(f"Erro: {erro}")
except DistanciaNegeativa as erro:
     print (f"Erro {erro}")