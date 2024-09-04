# Solicitar ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

try:
    # Verificar se o número é par ou ímpar
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
    
except:
    print("Entrada inválida. Por favor, insira um número inteiro válido.")