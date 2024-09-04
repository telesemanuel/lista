numeros = [ 1, 2, 3, 4 , 5, 6, 7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]

def primo(num):
    #Retorna True se num for um número primo, caso contrário, False.
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def listar_numeros_primos():
    # Criar uma lista com números de 1 a 20
    lista_numeros = list(range(1, 21))
    
    # Verificar quais números são primos
    primos = [num for num in lista_numeros if primo(num)]
    
    # Exibir os números primos
    print("Números primos de 1 a 20:\n")
    print(primos)

# Chamar a função para executar o programa
listar_numeros_primos()
