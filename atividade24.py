class Animal:
    def __init__(self, nome, especie, dieta):
        self.nome = nome
        self.especie = especie
        self.dieta = dieta
        self.saude = "Boa"
        self.local = None

class Habitat:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.animais = []

class Veterinario:
    def __init__(self, nome):
        self.nome = nome

    def cuidar(self, animal):
        animal.saude = "Boa"
        print(f"{self.nome} cuidou do {animal.nome}, a saúde está 100/100!")

class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def mover_animal(self, animal, habitat):
        if animal.local:
            animal.local.animais.remove(animal)
        habitat.animais.append(animal)
        animal.local = habitat
        print(f"{animal.nome} movido para {habitat.nome}")

class Zoologico:
    def __init__(self):
        self.animais = []
        self.habitats = []
        self.veterinarios = []
        self.funcionarios = []

    def cadastrar_animal(self):
        nome = input("Nome do animal: ")
        especie = input("Espécie: ")
        dieta = input("Dieta (carnívoro, herbívoro, onívoro): ")
        a = Animal(nome, especie, dieta)
        self.animais.append(a)
        print(f"Animal {nome} cadastrado!")

    def cadastrar_habitat(self):
        nome = input("Nome do habitat: ")
        tipo = input("Tipo do habitat: ")
        h = Habitat(nome, tipo)
        self.habitats.append(h)
        print(f"Habitat {nome} cadastrado!")

    def cadastrar_veterinario(self):
        nome = input("Nome do veterinário: ")
        v = Veterinario(nome)
        self.veterinarios.append(v)
        print(f"Veterinário {nome} cadastrado!")

    def cadastrar_funcionario(self):
        nome = input("Nome do funcionário: ")
        f = Funcionario(nome)
        self.funcionarios.append(f)
        print(f"Funcionário {nome} cadastrado!")

    def alimentar(self):
        nome = input("Qual animal alimentar? ")
        animal = next((a for a in self.animais if a.nome == nome), None)
        if animal:
            print(f"Alimentando {animal.nome} ({animal.dieta})")
        else:
            print("Animal não encontrado.")

    def cuidar_animal(self):
        nome_vet = input("Qual veterinário vai cuidar? ")
        vet = next((v for v in self.veterinarios if v.nome == nome_vet), None)
        nome_animal = input("Qual animal precisa de cuidado? ")
        animal = next((a for a in self.animais if a.nome == nome_animal), None)
        if vet and animal:
            vet.cuidar(animal)
        else:
            print("Veterinário ou animal não encontrado.")

    def mover(self):
        nome_func = input("Qual funcionário vai mover o animal? ")
        func = next((f for f in self.funcionarios if f.nome == nome_func), None)
        nome_animal = input("Qual animal mover? ")
        animal = next((a for a in self.animais if a.nome == nome_animal), None)
        nome_habitat = input("Pra qual habitat mover? ")
        habitat = next((h for h in self.habitats if h.nome == nome_habitat), None)
        if func and animal and habitat:
            func.mover_animal(animal, habitat)
        else:
            print("Funcionário, animal ou habitat não encontrado.")

zoo = Zoologico()

while True:
    print("\n1-Cadastrar animal\n2-Cadastrar habitat\n3-Cadastrar veterinário\n4-Cadastrar funcionário\n5-Alimentar animal\n6-Cuidar animal\n7-Mover animal\n8-Sair")
    op = input("Escolha: ")
    if op == "1":
        zoo.cadastrar_animal()
    elif op == "2":
        zoo.cadastrar_habitat()
    elif op == "3":
        zoo.cadastrar_veterinario()
    elif op == "4":
        zoo.cadastrar_funcionario()
    elif op == "5":
        zoo.alimentar()
    elif op == "6":
        zoo.cuidar_animal()
    elif op == "7":
        zoo.mover()
    elif op == "8":
        break
    else:
        print("Opção inválida")
