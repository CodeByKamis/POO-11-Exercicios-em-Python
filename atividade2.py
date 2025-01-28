class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def login(self):
        tentativa = input("Digite o seu nome: ")
        tentativa1 = int(input("Digite o número da conta: "))


        if tentativa != self.nome_titular or tentativa1 != self.numero_conta:
            print("Login incorreto!")
        else:
            print("Entrada permitida! Seja Bem-vindo(a)")


    def conta(self):
        decisao = int(input("Deseja realizar um depósito(1) ou saque(2)? "))



        if decisao == 1:
            valor = float(input("Digite o valor que deseja depositar? "))
            self.saldo += valor
            print(f"Depósito feito com sucesso, agora você possui R${self.saldo:.2f} como novo saldo")


        elif decisao == 2:
            valorzinho = float(input("Digite o valor que deseja sacar: "))
            if valorzinho > self.saldo:
                print("Impossível, esse valor é maior que o seu saldo disponível, tente um impréstimo com o banco, procure uma agencia mais próxima.")
            else:
                self.saldo -= valorzinho
                print(f"Saque realizado com sucesso, agora você possui R${self.saldo:.2f}.")
    
bank_kamis = ContaBancaria(143900, "kamila", 500.00)
bank_kamis.login()
bank_kamis.conta()