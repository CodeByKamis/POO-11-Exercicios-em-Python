import calendar
from datetime import datetime

class Calendario:
    def mostrar_mes(self):
        ano = int(input("Qual ano? "))
        mes = int(input("Qual mês? (1-12) "))
        if 1 <= mes <= 12:
            print(calendar.month(ano, mes))
        else:
            print("Mês inválido.")

    def verificar_feriado(self):
        data = input("Escreve uma data (dd/mm/aaaa): ")
        try:
            d = datetime.strptime(data, "%d/%m/%Y")
            feriados = {"01/01": "Ano Novo", "07/09": "Independência", "25/12": "Natal"}
            chave = d.strftime("%d/%m")
            if chave in feriados:
                print(f"{data} é feriado: {feriados[chave]}")
            else:
                print(f"{data} não é feriado.")
        except:
            print("Data errada.")

    def dif_dias(self):
        d1 = input("Primeira data (dd/mm/aaaa): ")
        d2 = input("Segunda data (dd/mm/aaaa): ")
        try:
            data1 = datetime.strptime(d1, "%d/%m/%Y")
            data2 = datetime.strptime(d2, "%d/%m/%Y")
            diff = abs((data2 - data1).days)
            print(f"Tem {diff} dias de diferença entre elas.")
        except:
            print("Data errada.")

cal = Calendario()

while True:
    print("\nCalendário Kamila")
    print("1 - Mostrar mês")
    print("2 - Ver se é feriado")
    print("3 - Diferença entre datas")
    print("4 - Sair")
    op = input("O que quer? ")
    if op == "1":
        cal.mostrar_mes()
    elif op == "2":
        cal.verificar_feriado()
    elif op == "3":
        cal.dif_dias()
    elif op == "4":
        print("byebye :P, até mais!")
        break
    else:
        print("Opção inválida.")
