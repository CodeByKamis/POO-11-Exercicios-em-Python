from datetime import datetime

class Tarefa:
    def __init__(self, titulo, prioridade, vencimento, status, categoria):
        self.titulo = titulo
        self.prioridade = prioridade
        self.vencimento = datetime.strptime(vencimento, "%d/%m/%Y")
        self.status = status
        self.categoria = categoria

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []

    def criar(self):
        t = input("Título da tarefa: ")
        p = input("Prioridade (alta, média, baixa): ")
        v = input("Data de vencimento (dd/mm/aaaa): ")
        s = input("Status (pendente, andamento, concluída): ")
        c = input("Categoria: ")
        self.tarefas.append(Tarefa(t, p, v, s, c))
        print("Tarefa criada!")

    def listar(self):
        for i, t in enumerate(self.tarefas):
            print(f"{i} - {t.titulo} | Prioridade: {t.prioridade} | Vence em: {t.vencimento.strftime('%d/%m/%Y')} | Status: {t.status} | Categoria: {t.categoria}")

    def editar(self):
        self.listar()
        i = int(input("Qual tarefa editar? "))
        if 0 <= i < len(self.tarefas):
            t = self.tarefas[i] #assim fica mais facil de chamar as tarefas
            t.titulo = input(f"Título ({t.titulo}): ") or t.titulo
            t.prioridade = input(f"Prioridade ({t.prioridade}): ") or t.prioridade
            venc = input(f"Vencimento ({t.vencimento.strftime('%d/%m/%Y')}): ") or t.vencimento.strftime('%d/%m/%Y')
            t.vencimento = datetime.strptime(venc, "%d/%m/%Y")
            t.status = input(f"Status ({t.status}): ") or t.status
            t.categoria = input(f"Categoria ({t.categoria}): ") or t.categoria
            print("Tarefa atualizada!")
        else:
            print("Índice inválido.")

    def excluir(self):
        self.listar()
        i = int(input("Qual tarefa excluir? "))
        if 0 <= i < len(self.tarefas):
            self.tarefas.pop(i)
            print("Tarefa excluída!")
        else:
            print("Índice inválido.")

    def filtrar(self):
        f = input("Filtrar por status ou prioridade? (status/prioridade) ").lower()
        if f == "status":
            status = input("Qual status? ")
            filtradas = [t for t in self.tarefas if t.status == status]
        else:
            prioridade = input("Qual prioridade? ")
            filtradas = [t for t in self.tarefas if t.prioridade == prioridade]
        for t in filtradas:
            print(f"{t.titulo} - Status: {t.status} - Prioridade: {t.prioridade}")

gerenciador = GerenciadorTarefas()

while True:
    print("\n1-Criar tarefa\n2-Editar tarefa\n3-Excluir tarefa\n4-Listar tarefas\n5-Filtrar\n6-Sair")
    op = input("Escolha: ")
    if op == "1":
        gerenciador.criar()
    elif op == "2":
        gerenciador.editar()
    elif op == "3":
        gerenciador.excluir()
    elif op == "4":
        gerenciador.listar()
    elif op == "5":
        gerenciador.filtrar()
    elif op == "6":
        break
    else:
        print("Opção inválida")
