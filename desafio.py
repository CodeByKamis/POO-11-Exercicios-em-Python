class Tarefa:
    def __init__(self, nome, responsavel, prazo):
        self.nome = nome
        self.responsavel = responsavel
        self.prazo = prazo
        self.status = "pendente"

class Fornecedor:
    def __init__(self, nome, servico):
        self.nome = nome
        self.servico = servico

class Pagamento:
    def __init__(self, descricao, valor, vencimento):
        self.descricao = descricao
        self.valor = valor
        self.vencimento = vencimento

class Evento:
    def __init__(self, nome, data, hora, local):
        self.nome = nome
        self.data = data
        self.hora = hora
        self.local = local
        self.tarefas = []
        self.fornecedores = []
        self.pagamentos = []

    def mostrar_detalhes(self):
        print(f"\nEvento: {self.nome}")
        print(f"Data: {self.data} | Hora: {self.hora} | Local: {self.local}")
        print("\nTarefas:")
        for t in self.tarefas:
            print(f"- {t.nome} | Resp: {t.responsavel} | Prazo: {t.prazo} | Status: {t.status}")
        print("\nFornecedores:")
        for f in self.fornecedores:
            print(f"- {f.nome} ({f.servico})")
        print("\nPagamentos:")
        for p in self.pagamentos:
            print(f"- {p.descricao} | R${p.valor} | Vencimento: {p.vencimento}")

eventos = []

def criar_evento():
    nome = input("Nome do evento: ")
    data = input("Data: ")
    hora = input("Hora: ")
    local = input("Local: ")
    evento = Evento(nome, data, hora, local)
    eventos.append(evento)
    print("Evento criado!")

def listar_eventos():
    for i, e in enumerate(eventos):
        print(f"{i} - {e.nome} | {e.data} | {e.local}")

def adicionar_tarefa():
    if not eventos:
        print("Nenhum evento ainda.")
        return
    listar_eventos()
    idx = int(input("Escolhe o número do evento: "))
    nome = input("Nome da tarefa: ")
    resp = input("Responsável: ")
    prazo = input("Prazo: ")
    tarefa = Tarefa(nome, resp, prazo)
    eventos[idx].tarefas.append(tarefa)
    print("Tarefa adicionada!")

def adicionar_fornecedor():
    if not eventos:
        print("Nenhum evento ainda.")
        return
    listar_eventos()
    idx = int(input("Escolhe o número do evento: "))
    nome = input("Nome do fornecedor: ")
    serv = input("Serviço dele: ")
    fornecedor = Fornecedor(nome, serv)
    eventos[idx].fornecedores.append(fornecedor)
    print("Fornecedor adicionado!")

def adicionar_pagamento():
    if not eventos:
        print("Nenhum evento ainda.")
        return
    listar_eventos()
    idx = int(input("Escolhe o número do evento: "))
    desc = input("Descrição do pagamento: ")
    valor = float(input("Valor: R$"))
    venc = input("Data de vencimento: ")
    pagamento = Pagamento(desc, valor, venc)
    eventos[idx].pagamentos.append(pagamento)
    print("Pagamento registrado!")

def ver_detalhes_evento():
    if not eventos:
        print("Nenhum evento ainda.")
        return
    listar_eventos()
    idx = int(input("Escolhe o número do evento: "))
    eventos[idx].mostrar_detalhes()

while True:
    print("\n--- SISTEMA DE EVENTOS DA KAMILA ---")
    print("1 - Criar evento")
    print("2 - Adicionar tarefa")
    print("3 - Adicionar fornecedor")
    print("4 - Adicionar pagamento")
    print("5 - Ver detalhes do evento")
    print("6 - Sair")
    escolha = input("\nO que você quer fazer? ")

    if escolha == "1":
        criar_evento()
    elif escolha == "2":
        adicionar_tarefa()
    elif escolha == "3":
        adicionar_fornecedor()
    elif escolha == "4":
        adicionar_pagamento()
    elif escolha == "5":
        ver_detalhes_evento()
    elif escolha == "6":
        print("Saindo... Até a próxima!")
        break
    else:
        print("Opção inválida, tenta de novo.")
