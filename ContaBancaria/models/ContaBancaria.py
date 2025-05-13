import time

class ContaBancaria:
   '''
   Classe que implementa métodos para manipular uma conta bancária.add()
   Atributos: títular(str), saldo(float), limite(float) e histótico (lista de dicionários)
   
   Obs.: Operações no histórico: 0-sacar, 1-depositar, 2-transferir.

   '''
   def __init__(self, titular, saldo, limite, historico):
        '''
        Construtor da classe conta bancária
        '''
        self.titular = titular  
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

   def depositar(self, valor):
        '''
        Método que realiza o deposito na conta bancária.

        Entrada: valor(float)
        Return: True se a operação foi realizada com sucesso, False, se a operação não foi realizada com sucesso.
        '''
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": 1,
                                    "remetente":self.titular,
                                     "destinatario": "",
                                     "valor": valor,
                                    "saldo": self.saldo,
                                    "dataetempo":int(time.time()) })
            return True

        else:
            print(f"O valor {valor} é inválido!")
            return False 
        
   def sacar(self, valor):    
        '''
        Método que realiza o saque da conta báncaria.

        Entrada: valor(float)
        Retunr: True se a operação foi realizada com sucesso.False, se a operação não foi realizada com sucesso.
        '''
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": 0,
                                    "remetente":self.titular,
                                     "destinatario": "",
                                     "valor": valor,
                                    "saldo": self.saldo,
                                    "dataetempo":int(time.time()) })
            print("Saque Realizado!")
            return True
   
        else:
            a = input(f"Deseja utilizar o Limite? (R$ {self.limite}) [s,n]")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque Realizado!")
                    return True
                
                else:
                    print("Saldo e limite insuficientes!")
                    return False
            else: 
                print("Saque do saldo e limite Cancelado!")
                return False
                    
   def exibirHistorico(self):
        print("Histórico de Transações:")
        for transacao in self.historico:

            dt = time.localtime(transacao["dataetempo"])

            print("op.: ", transacao["operacao"], 
                   "remetente: ", transacao["remetente"], 
                    "destinatario: ",  transacao["destinatario"],
                   "saldo: ",  transacao["saldo"],
                    "valor: ", transacao["valor"],
                    "hora e data: ", 
                    f" {dt.tm_hour} : {dt.tm_min} : {dt.tm_sec} . {dt.tm_mday} / {dt.tm_mon} / {dt.tm_year}")
            
   def transferencia(self, destinatario, valor):
       if self.sacar (valor, destinatario, titular):
            destinatario.depositar(valor, self.titular)
            return True
            return False