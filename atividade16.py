class RedeSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = []
        self.comentarios = []

    def add_usuario(self):
        nome = input("Me diz seu nome pra cadastrar: ")
        if nome not in self.usuarios:
            self.usuarios[nome] = {"amigos": set()}
            print(f"{nome} cadastrado com sucesso!")
        else:
            print(f"{nome} já tá cadastrado.")

    def add_amigo(self):
        user = input("Quem tá adicionando amigo? ")
        amigo = input("Qual o nome do amigo? ")
        if user in self.usuarios and amigo in self.usuarios:
            self.usuarios[user]["amigos"].add(amigo)
            self.usuarios[amigo]["amigos"].add(user)
            print(f"{user} e {amigo} agora são amigos!")
        else:
            print("Alguém aí não existe na rede.")

    def postar(self):
        user = input("Quem vai postar? ")
        if user in self.usuarios:
            msg = input("Escreve sua mensagem: ")
            self.posts.append({"autor": user, "msg": msg})
            print(f"{user} postou: {msg}")
        else:
            print("Esse usuário não existe.")

    def comentar(self):
        user = input("Quem vai comentar? ")
        if user not in self.usuarios:
            print("Usuário não existe.")
            return
        if not self.posts:
            print("Não tem nenhum post ainda.")
            return
        print("Posts:")
        for i, post in enumerate(self.posts):
            print(f"{i} - {post['autor']}: {post['msg']}")
        idx = int(input("Qual post quer comentar (número)? "))
        if 0 <= idx < len(self.posts):
            cm = input("Escreve seu comentário: ")
            self.comentarios.append({"post": idx, "autor": user, "coment": cm})
            print(f"{user} comentou no post {idx}: {cm}")
        else:
            print("Post inválido.")

    def buscar_usuario(self):
        nome = input("Quem você quer procurar? ")
        if nome in self.usuarios:
            amigos = self.usuarios[nome]["amigos"]
            if amigos:
                print(f"{nome} tem esses amigos: {', '.join(amigos)}")
            else:
                print(f"{nome} não tem amigos ainda.")
        else:
            print("Usuário não encontrado.")

rede = RedeSocial()

while True:
    print("\nRede Social da Kamis")
    print("\nEscolhe uma opção :D")
    print("1 - Cadastrar usuário")
    print("2 - Adicionar amigo")
    print("3 - Fazer post")
    print("4 - Comentar post")
    print("5 - Buscar usuário")
    print("6 - Sair")
    op = input("O que você quer? ")
    if op == "1":
        rede.add_usuario()
    elif op == "2":
        rede.add_amigo()
    elif op == "3":
        rede.postar()
    elif op == "4":
        rede.comentar()
    elif op == "5":
        rede.buscar_usuario()
    elif op == "6":
        print("Tchau! Volta sempre :)")
        break
    else:
        print("Escolha inválida.")
