class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def adicionar_consulta(self, consulta):
        self.historico_consultas.append(consulta)
        print(f"Consulta '{consulta}' adicionada ao histórico de {self.nome}.")

    def exibir_consultas(self):
        if not self.historico_consultas:
            print(f"O paciente {self.nome} ainda não realizou nenhuma consulta.")
        else:
            print(f"Histórico de consultas do paciente {self.nome}:")
            for i, consulta in enumerate(self.historico_consultas, 1):
                print(f"{i}. {consulta}")


paciente = Paciente("Jumilya", 25) 

paciente.adicionar_consulta("Cardiologia")
paciente.adicionar_consulta("Dermatologia")
paciente.exibir_consultas()