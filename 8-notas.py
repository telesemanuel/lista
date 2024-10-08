import os

notas = []

while True:
    opcao = input("1 para inserir nota ou 2 para calcular média: ")
    os.system("cls")
    match opcao:
        case "1":
            try:
                nova_nota = float(input("Informe um valor de 0 a 10: ").replace(",","."))
                if nova_nota >= 0 and nova_nota <= 10:
                    notas.append(nova_nota)
                    print('Nota inserida com sucesso.')
                else:
                    print("Nota Inválida")
            except Exception as e:
                print(f"Não foi possível inserir nota {e}")
            finally:
                continue
        case "2":
            break
        case _:
            print("Opcão Inválida.")
            continue
print(f"Média: {(sum(notas)/len(notas)):,.2f}")