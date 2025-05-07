class Veiculos:
    def __init__(self, modelo, marca, ano, cor, velocidade, latitude, longetude, placa):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude
        self.placa = placa

    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.latitude + 1
        self.alterarLatitude(nova_latitude)
        print(f"O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h")

    def frenagem(self): 
        if self.velocidade >0:
            self.velocidade -= 10
        print(f"O carro de placa {self.placa}, irá reduzir a velocidade {self.velocidade} km/h")

    def mostrarInfos(self): 
        print(f" O veiculo {self.modelo}, de placa {self.placa}, está a {self.velocidade} km/h")
        print("Lat.: {self.latitude}, Long.: {self.longetude}")

    def alterarPlaca(self, placa):
        self.placa = placa

    def alterarModelo(self, modelo):
        self.modelo = modelo

    def alterarAno(self, ano):
        self.ano = ano
    
    def alterarCor(self, cor):
        self.cor = cor

    def alterarLatitude(self, latitude):
        self.latitude = latitude

    def alterarLongetude(self, longetude):
        self.longetude = longetude

    def obterPlaca(self):
        return self.placa
    def obterAno(self):
        return self.ano
    def obterModelo(self):
        return self.modelo
    def obterCor(self):
        return self.cor
    