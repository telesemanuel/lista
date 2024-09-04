# Solicitar ao usuário um número inteiro positivo
import time
numero = int(input("Digite um número inteiro positivo: "))

try:
    # Verificar se o número é positivo
    if numero <= 0:
            print("Por favor, insira um número inteiro positivo.")
    else:

        # Exibir a contagem regressiva
        for i in range(numero, -1, -1):
            print(i)
            time.sleep(0.5)
        print("Fim!")
    
except:
    print("Entrada inválida. Por favor, insira um número inteiro positivo.")