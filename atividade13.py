class Agenda:
    def __init__(self):
        self.lista_nome = []
        self.lista_telefonica = []


    def adicionar (self):
        lista_completa = list(zip(self.lista_nome, self.lista_telefonica))
        while True:
            print("Vamos adicionar novos contatos!")
            addnome = input("Adicione o nome do contato: ")
            addnum = input("Adicione o número do contato")
            self.lista_nome.append(addnome)
            self.lista_telefonica.append(addnum)
            print(f"Essa é a sua lista de contato {list(zip(self.lista_nome, self.lista_telefonica))}")
            pergunta = input("Deseja adicionar mais algum contato? Y/N")
            if pergunta == "N":
                False
                break
            elif pergunta == "Y":
                continue

    def editar(self):
        lista_completa = list(zip(self.lista_nome, self.lista_telefonica))
        while True:
            perguntinha = input("Você deseja fazer uma edição na lista telefonica Y/N?")
            if perguntinha == "N":
                break
            elif perguntinha == "Y":
                print(f"\nSua lista de contatos: \n{lista_completa}")
                pergunta = input("Você deseja editar nome ou número:").lower()
                if pergunta == "nome":
                    indexnome = input("Qual é o index do nome que você gostaria de editar?"))
                    edicaonome = input("Coloque aqui a sua edição: ")
                    self.lista_nome[indexnome] = edicaonome
                    print(f"Edição feita com sucesso! Veja sua lista telefonica atualizada:\n {lista_completa}")

                elif pergunta == "número":
                    indexnumero = input("Qual é o index do número que você gostaria de editar?")
                    edicaonumero = input("Coloque aqui a sua edição: ")
                    self.lista_nome[indexnumero] = edicaonumero
                    print(f"Edição feita com sucesso! Veja sua lista telefonica atualizada:\n {lista_completa}")

    def excluir (self):
        lista_completa = list(zip(self.lista_nome, self.lista_telefonica))
        while True:
            perguntinha = input("Você deseja excluir algum número da lista telefonica? Y/N").lower()
            if perguntinha == "n":
                break
            elif perguntinha == "y":
                continue

            print(f"\nSua lista de contatos: \n{lista_completa}")
            remover = input("Digite o index do contato que você deseja remover: \n")
            removendo = lista_completa.pop(remover)
            print(f"Contato removido com sucesso!\n Veja sua lista de contatos atualizada: \n{removendo}")
    
    def pesquisar (self):
        lista_completa = list(zip(self.lista_nome, self.lista_telefonica)).lower()
        while True:
            perguntinha = input("Você deseja pesquisar algum número na lista telefonica? Y/N").lower()
            if perguntinha == "n":
                break
            elif perguntinha == "y":
                pesquisar = input("\nPesquise: (nome ou número) ").lower()
                encontrei = False
                for pesquisa in lista_completa:
                    if pesquisa == pesquisar:
                        print(f"{pesquisar} foi encontrado na lista")
                        qualindex = self.lista_completa.index(pesquisar)
                        print(lista_completa[qualindex])
                    else:
                        print("Esse contato não existe na sua lista")

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

# class Agenda:
#     def __init__(self):
#         self.lista_nome = []
#         self.lista_telefonica = []

#     def adicionar(self):
#         while True:
#             print("Vamos adicionar novos contatos!")
#             addn = input("Adicione o nome do contato: ")
#             addnm = input("Adicione o número do contato: ")
#             self.lista_nome.append(addn)
#             self.lista_telefonica.append(addnm)
#             print(f"Essa é a sua lista de contatos: {list(zip(self.lista_nome, self.lista_telefonica))}")
#             pergunta = input("Deseja adicionar mais algum contato? Y/N: ").lower()
#             if pergunta == "n":
#                 break
#             elif pergunta == "y":
#                 continue

#     def editar(self):
#         while True:
#             print(f"\nSua lista de contatos: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
#             pergunta = input("Você deseja editar nome ou número? (Digite 'nome' ou 'número'): ").lower()
#             if pergunta not in ["nome", "número"]:
#                 print("Opção inválida. Por favor, digite 'nome' ou 'número'.")
#                 continue

#             if pergunta == "nome":
#                 indexnome = int(input("Qual é o índice do nome que você gostaria de editar? "))
#                 if 0 <= indexnome < len(self.lista_nome):
#                     edicaonome = input("Coloque aqui a sua edição: ")
#                     self.lista_nome[indexnome] = edicaonome
#                     print(f"Edição feita com sucesso! Veja sua lista de contatos atualizada:\n {list(zip(self.lista_nome, self.lista_telefonica))}")
#                 else:
#                     print("Índice inválido!")
#             elif pergunta == "número":
#                 indexnumero = int(input("Qual é o índice do número que você gostaria de editar? "))
#                 if 0 <= indexnumero < len(self.lista_telefonica):
#                     edicaonumero = input("Coloque aqui a sua edição: ")
#                     self.lista_telefonica[indexnumero] = edicaonumero
#                     print(f"Edição feita com sucesso! Veja sua lista de contatos atualizada:\n {list(zip(self.lista_nome, self.lista_telefonica))}")
#                 else:
#                     print("Índice inválido!")

#             pergunta = input("Deseja editar outro contato? Y/N: ").lower()
#             if pergunta == "n":
#                 break

#     def excluir(self):
#         while True:
#             print(f"\nSua lista de contatos: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
#             try:
#                 remover = int(input("Digite o índice do contato que você deseja remover: "))
#                 if 0 <= remover < len(self.lista_nome):
#                     self.lista_nome.pop(remover)
#                     self.lista_telefonica.pop(remover)
#                     print(f"Contato removido com sucesso! Veja sua lista de contatos atualizada: \n{list(zip(self.lista_nome, self.lista_telefonica))}")
#                 else:
#                     print("Índice inválido!")
#             except ValueError:
#                 print("Por favor, digite um número válido.")
                
#             pergunta = input("Deseja excluir outro contato? Y/N: ").lower()
#             if pergunta == "n":
#                 break

#     def pesquisar(self):
#         while True:
#             perguntinha = input("Você deseja pesquisar algum número na lista telefônica? Y/N: ").lower()
#             if perguntinha == "n":
#                 break
#             elif perguntinha == "y":
#                 pesquisar = input("\nPesquise (nome ou número): ").lower()
#                 encontrei = False
#                 for nome, telefone in zip(self.lista_nome, self.lista_telefonica):
#                     if pesquisar == nome.lower() or pesquisar == telefone.lower():
#                         print(f"Encontrado! Nome: {nome}, Telefone: {telefone}")
#                         encontrei = True
#                         break
#                 if not encontrei:
#                     print(f"'{pesquisar}' não foi encontrado na lista.")

# agenda = Agenda()

# while True:
#     print("Bem-vindo à sua lista telefônica! Como podemos te ajudar?")
#     pergunta = input("(01) Adicionar contato\n(02) Editar contato\n(03) Excluir contato\n(04) Pesquisar contato\n(05) Sair\n")
    
#     if pergunta == "01":
#         agenda.adicionar()

#     elif pergunta == "02":
#         agenda.editar()

#     elif pergunta == "03":
#         agenda.excluir()

#     elif pergunta == "04":
#         agenda.pesquisar()

#     elif pergunta == "05":
#         print("Ok, até logo.")
#         break
