class Banco:
    def __init__(self, dinheiro):
        self.dinheiro = dinheiro

    def cadastro_cliente(self):
        abrir_conta = input("Seja bem-vindo(a) ao banco da Kamila, vamos abrir uma conta para você. escreva 'Não desejo' caso não queira abrir uma conta")
        if abrir_conta == "Não desejo":
            print("Tudo bem, tchau.")
        else:
            nome = input("Digite o seu nome: ")
            cpf = input("Digite o seu cpf: ")
            idade = int(input("Digite sua idade atual: "))
            if idade >=18:
                print("Você é maior de idade, vamos cadastrar você agora mesmo no sistema.")
                print(f"Informações cadastradas:\n Nome: {nome};\n CPF: {cpf},\n Idade atual: {idade}") 
            elif idade < 18:
                print("Vamos criar uma conta infantil para você, digite o abaixo o nome dos seus responsáveis e cpf")
                cpf_m = input("CPF mãe: ")
                cpf_p = input("CPF pai: ")
                print("Informações recebidas com sucesso, vamos cadastrar tudo agora!")
                print(f"Informações cadastradas: \nNome: {nome};\n CPF pessoal: {cpf};\n Idade atual: {idade};\n CPF da mãe: {cpf_m};\n CPF do pai:{cpf_p}.")
        
    def saque(self):
        print(f"Você tem R${self.dinheiro} de saldo bancário")
        sacar = float(input("Digite o valor que deseja sacar: R$"))
        if sacar > self.dinheiro:
            print(f"Sinto muito, mas não é possível sacar esse valor pois você possui apenas R${self.dinheiro} reais.")
        else:
            self.dinheiro -= sacar
            print(f"Você sacou: R${sacar} reais. Sua conta possui R${self.dinheiro} reais.")
        
    def deposito(self):
        print(f"Você tem R${self.dinheiro} de saldo bancário")
        depositar = float(input("Digite o valor que deseja depositar: R$"))
        self.dinheiro += depositar
        print(f"Você depositou: R${depositar} reais. Sua conta possui R${self.dinheiro} reais.")
        
    def transferencia(self):
        print(f"Você tem R${self.dinheiro} de saldo bancário")
        transferir = float(input("Digite quanto você deseja transferir: R$"))
        if transferir > self.dinheiro:
            print(f"Sinto muito, mas não é possível transferir R${transferir} reais, pois você possui apenas R${self.dinheiro} reais em seu saldo bancário.")
        else:
            quem = input(f"Digite o número da conta que deseja transferir R${transferir}")
            self.dinheiro -= transferir
            print(f"Tranferência realizada com sucesso! Você transferiu R${transferir} reais para a conta: {quem}")
            print(f"O saldo bancário atual da sua conta é de: {self.dinheiro}")

banco = Banco(500.00)
funcao = input("Bem-vindo(a) ao banco da Kamila!!\n O que você deseja realizar:\n abrir conta(1);\n realizar saque(2);\n realizar depósito(3);\n realizar transferência(4)\n")
if funcao == "1":
    banco.cadastro_cliente()
elif funcao == "2":
    banco.saque()
elif funcao == "3":
    banco.deposito()
elif funcao == "4":
    banco.transferencia()