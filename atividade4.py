class Aluno:
    def __init__ (self, nome, matricula, nota1,nota2,nota3):
        self.nome=nome
        self.matricula=matricula
        self.nota1=nota1
        self.nota2=nota2
        self.nota3=nota3

    def calculo_nota(self):
        calculo = (self.nota1+self.nota2+self.nota3)/3
        if calculo >=5:
            return(f"A(O) aluna(o) {self.nome} está: APROVADA(O)")
        elif calculo <5:
            return(f"A(O) aluna(o) {self.nome} está:REPROVADA(O)")
        

matriculinha = Aluno ("kamila", 112, 100, 100, 100)
print(matriculinha.calculo_nota())