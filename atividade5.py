class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    def salario_liquido (self):
        imposto = 2.5 / 100
        beneficio = 150
        salario_final = self.salario - (self.salario * imposto) - beneficio
        return(f"O salário da funcionária {self.nome} é de R${salario_final}")

funcionario = Funcionario("kamila", 1500, "soluções digitais")
print(funcionario.salario_liquido())
    
