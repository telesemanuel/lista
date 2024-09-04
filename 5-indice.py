lista_nomes = ["Ana","Carlos","Fernanda","Gabriel","Isabela","João","Maria","Pedro","Sofia","Tiago"]

print("Lista de Nomes:")
for i, nome in enumerate(lista_nomes):
    print(f"Índice {i + 1}: {nome}")

try:
    # Solicitar ao usuário um número inteiro para o índice
        indice = int(input("Digite o índice do nome que deseja ver: "))

    # Converter o índice para o intervalo da lista (começa em 0)
        indice_corrigido = indice - 1
        
    # Verificar se o índice está dentro do intervalo válido
        if 0 <= indice_corrigido < len(lista_nomes):
            # Exibir o nome correspondente ao índice
            print(f"O nome no índice {indice} é: {lista_nomes[indice_corrigido]}")
        else:
            print("Índice fora do intervalo válido. Por favor, insira um número entre 1 e 10.")
    
except:
    print("Entrada inválida. Por favor, insira um número inteiro.")