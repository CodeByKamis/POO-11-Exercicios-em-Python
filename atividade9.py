class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def historico_consultas(self):
        lista = ["cardiologia", "oncologia", "gastroenterologia", "dermatologia", "neurologia", "psiquiatria"]
        print(f"Esses são os exames que {self.nome} precisa fazer: \n{lista}")
        adicionar = input("Deseja adicionar mais algume exame a lista?")
        if adicionar == "sim":
            novo_exame = input("Escreva o nome do exame que deseja adicionar: ")
            lista.append(novo_exame)
            print(f"Lista de exames atualizada:\n {lista}")

        else:
            print("Nenhum exame será adicionado!")

paciente = Paciente("jumilya", "25")
paciente.historico_consultas()