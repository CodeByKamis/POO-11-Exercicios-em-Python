class Agenda:
    def __init__(self):
        self.lista_nome = []
        self.lista_telefonica = []


    def adicionar (self):
        while True:
            print("Vamos adicionar novos contatos!")
            addnome = input("Adicione o nome do contato: ")
            addnum = input("Adicione o número do contato")
            self.lista_nome.append(addnome)
            self.lista_telefonica.append(addnum)
            print(f"Essa é a sua lista de contato: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
            pergunta = input("Deseja adicionar mais algum contato? Y/N")
            if pergunta == "N":
                break
            elif pergunta == "Y":
                continue

    def editar(self):
        while True:
            print(f"Essa é a sua lista de contato: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
            perguntinha = input("Você deseja editar nome ou numero (escreva mínusculo e sem acentuação)?").lower()
            if perguntinha == "nome":
                indexnome = int(input("Qual é o index do nome que você gostaria de editar?"))
                if 0 <= indexnome < len(self.lista_nome):
                    editarnome = input ("Coloque aqui a sua edição: \n")
                    self.lista_nome[indexnome] = editarnome
                    print(f"Edição feita com sucesso! Veja sua lista telefonica atualizada: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
                else:
                    print("Acho que você errou o índice :c")
            elif perguntinha == "numero":
                indexnumero = int(input("Qual é o index do número que você gostaria de editar?"))
                if 0<= indexnumero <len (self.lista_telefonica):
                    editarnumero = input("Coloque aqui a sua edição: \n")
                    self.lista_telefonica[indexnumero] = editarnumero
                    print(f"Edição feita com sucesso! Veja sua lista telefonica atualizada: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
                else:
                    print("Acho que você errou o índice :c")
            pergunta = input ("Deseja editar outro contato? Y/N")
            if pergunta == "N":
                break
            

    def excluir (self):
        while True:
            perguntinha = input("Você deseja excluir algum número da lista telefonica? Y/N")
            if perguntinha == "N":
                break
            elif perguntinha == "Y":
                try:
                    print(f"\nSua lista de contatos: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
                    remover = int(input("Digite o index do contato que você deseja remover: \n"))
                    if 0<= remover <len(self.lista_nome):
                        self.lista_nome.pop(remover)
                        self.lista_telefonica.pop(remover)
                        print(f"Contato removido com sucesso!\n Veja sua lista de contatos atualizada: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
                    else:
                        print("Não existe número nesse indice ou ele é inválido!")
                except ValueError:
                    print("Algo deu errado, entte com as respostas corretas ")
            
    def pesquisar (self):
        while True:
            perguntinha = input("Você deseja pesquisar algum número na lista telefonica? Y/N")
            if perguntinha == "N":
                break
            elif perguntinha == "Y":
                pesquisar = input("\nPesquise com nome ou número corretamente: ").lower()
                achado = False
                for nome, telefone in zip(self.lista_nome, self.lista_telefonica):
                    if pesquisar == nome.lower() or pesquisar == telefone.lower():
                        print(f"contato encontrado!\n Nome: {nome},\n Telefone: {telefone}")
                        achado = True
                        break
                    if not achado:
                        print(f"{achado} infelizmente não foi encontrado na sua lista de contatos :c")


agenda = Agenda()
while True:
    print("Bem-vindo a essa lista telefonica, como podemos te ajudar?")
    pergunta = input("(01)Adicionar contato\n(02)Editar contato\n(03)Excluir contato\n(04)Pesquisar contato\n(05)Sair\n")
    if pergunta == "01":
        agenda.adicionar()

    elif pergunta == "02":
        agenda.editar()

    elif pergunta == "03":
        agenda.excluir()

    elif pergunta == "04":
        agenda.pesquisar()

    elif pergunta == "05":
        print("Ok, até logo.")
        break



    
    # def excluir
    # def pesquisar
#LISTA FEITE CORRETAMENTE 
