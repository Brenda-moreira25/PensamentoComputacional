def __init__(self, produto: str):
    self.__produto ==  produto
    self.__usd_brl = 5.05 
    self.__eur_brl = 6.14 
    self.__eur_usd = 1.22 
    
def converte_preco_para_usd(self, produto):
    produto.set_preco(produto.get_preco()/self.__usd_brl)
    produto.set_moeda ('USD')    
    return True

def converte_preco_para_eur(self, produto):
    produto.set_preco(produto.get_preco/self.__eur_brl)
    produto.set_moeda('USD')
    return True

def converte_preco_para_brl(self, produto): 
    produto.set_preco(produto.get_preco/eur_usd)
    produto.set_moeda('USD')
    return True
     

