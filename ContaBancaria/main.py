from models.ContaBancaria import ContaBancaria

<<<<<<< Updated upstream
banco = []
=======
#Irá gerar um tipo de lista
banco = []

#Irá adicionar informações a lista vínculada banco.
banco.append(ContaBancaria("Arthur", 1000, 2000, []))
banco.append(ContaBancaria("Lauren", 100, 200, []))
banco.append(ContaBancaria("Lucas", 500, 1000, []))

titular = input("Informe o titular da conta: ")

#Método para verificar as opções de conta que contém em banco.
for conta in banco:
    if conta.titular == titular:
        print(f"O {titular} é o titular da conta, e tem R$ {conta.saldo} em conta, com um limite de R$ {conta.limite}")

while True:

    print(f"Operações disponiveis:" +
          "Sacar: 0" +
          "Depositar: 1" +
          "Transferir: 2")

    operacao = int(input("Informe a operação desejada: [0, 1, 2]"))

    if operacao == 0:
        valor.saque = float(input("Qual o valor para saque: "))
        conta.saldo  = conta.saldo - valor.saque
        print(f"Saque realizado de {valor.saque}")

    elif operacao == 1:
        valor.deposito = float(input("Qual o valor para deposito: "))
        conta.saldo = conta.saldo + valor.deposito
        print(f"Deposito realizado no valor de R$ {conta.depositar}")

    else:
        valor.transferencia = float(input("Qual o valor de transferencia: "))
        valor.transferencia = valor.transferencia
        print(f"Transferencia realizada no valor de R$ {conta.transferir}")
>>>>>>> Stashed changes

banco.append(ContaBancaria( "Lauren", 100, 200, []))
banco.append(ContaBancaria( "Lucas", 100, 200, []))

<<<<<<< Updated upstream
while True:

    n = input("Deseja realizar uma operção: [s,n] ")
   
    if n == "s" :
        print("Digite a operação desejada sendo que :", "Sacar: 0 ", 
                              "depositar: 1", 
                              "trasnferir: 2")
        resposta1 = (input())
        
        if resposta1 == "0":
            titular = input("Digite o titular que deseja sacar: ")
            valor = float(input("Quanto deseja sacar: "))
            for conta in banco:
                if conta.titular == titular:
                    conta.sacar(valor)

        elif resposta1 == "1":
                titular = input("Digite o titular que deseja depositar: ")
                valor = float(input("Quanto deseja depositar: "))
                for conta in banco:
                    if conta.titular == titular:
                        conta.depositar()
            
        elif resposta1 == "2":
            titular = input("Digite o titular que deseja trasnferir: ")
            valor = float(input("Quanto deseja trsnferir: "))
            for conta in banco:
                    if conta.titular == titular:
                        conta.transferencia()     
                        break                      
    elif n == "n":
        print("Operação não realizada/selecionada")
        
   
=======
    break
>>>>>>> Stashed changes
