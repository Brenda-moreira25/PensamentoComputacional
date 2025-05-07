from models.Veiculos import Veiculos

gol = Veiculos("Gol Copa", "Volkswagem", 2006, "Amarelo", 0, 0, 0, "IED-1010")
gol.mostrarInfos()

gol.acelerar()
gol.mostrarInfos()

gol.frenagem()
gol.mostrarInfos()

gol.alterarPlaca("IND1A10")
gol.mostrarInfos()
print(gol.placa)
print(gol.obterPlaca())

gol.alterarModelo("PALIO")
gol.mostrarInfos
print(gol.modelo)

gol.alterarAno("2011")
gol.mostrarInfos
print(gol.ano)

gol.alterarCor("Vermelho")
gol.mostrarInfos
print(gol.cor)


