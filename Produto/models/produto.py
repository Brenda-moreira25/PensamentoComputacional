from .produto import produto

class produto:

    #Método de atribuição
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"

    #Método strings de informações 
    def __str__(self):
        infos =  f"nome: {self.__nome}\n"
        infos +=  f"preco: {self.__preco}\n"
        infos +=  f"moeda: {self.__moeda}\n"
        infos +=  f"tipoAlimenticio: {self.__tipoAlimenticio}\n"
        infos +=  f"tipoEletronico: {self.__tipoEletronico}\n"
        return infos
    
    #Método de funções a serem executadas
    def __init__(self, verdura: str, fruta: str, mistura: str, tipoAlimenticio: str, 
                 tipoEletronico: str, tv: str, radio: str):
        self.__verdura = verdura
        self.__fruta = fruta
        self.__mistura = mistura
        self.__tipoAlimenticio = tipoAlimenticio
        self.__tipoEletronico = tipoEletronico
        self.__radio = radio
        self.__tv = tv

#Método para retornar o nome
    def get_nome(self):
        return self.__nome

#Método 
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco
    
    def get_moeda(self):
        return self.__moeda
    
    def set_moeda(self, moeda):
        self.__moeda = moeda
         
   

    

