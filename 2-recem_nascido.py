 # Solicita ao usuário o peso do bebê em quilogramas
peso = int(input("\nDigite o peso do bebê(em gramas): "))

try:
    # Verificar se o peso em gramas é menor que 2500 gramas
    if peso < 2500:
            print("\nO bebê precisa ficar internado.\n")
    else:
            print("\nO bebê está com o peso normal.\n")
    
except:
     print("Entrada inválida. Por favor, insira um número válido.")