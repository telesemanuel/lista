import os
from datetime import date

eventos = []

dia = date.today().day
mes = date.today().month
ano = date.today().year

while True:
    opcao = input("1 para cadastrar evento 2 para se inscrever: ")
    os.system("cls")
    match opcao:
        case "1":
            evento = {}
            try:
                evento["nome"] = input("Informe o nome do evento: ")
                evento["censura"] = int(input("Informe a classificação indicativa do evento: "))
                eventos.append(evento)
                print("Evento cadastrado com sucesso.")
            except Exception as e:
                print(f"Não foi possível cadastrar evento. {e}.")
            finally:
                continue
        case "2":
            nome = input("Informe o seu nome: ")
            idade = int(input("Informe sua idade: "))
            while True:
                print(f"\n{"&"*30} EVENTOS {"&"*30}")
                for i in range(len(eventos)):
                    print(f"Código do evento: {i}")
                    for campo in eventos[1]:
                        print(f"{campo.captalize()}:{eventos[i].get(campo)}.")
                    print("-"*30)
                try:
                    