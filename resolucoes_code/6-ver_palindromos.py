## 6 - Verificando Palíndromos 🔄

# Descrição: Vamos testar se uma palavra é um palíndromo?! 
# Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# O que aprenderemos?
# * Manipulação de strings em Python, especialmente invertendo uma string.
# * Compreensão de como comparar a string original com sua versão invertida para determinar se é um palíndromo.
# * Introdução ao conceito de palíndromos e sua aplicação em problemas de programação.
# Um palíndromo é uma palavra que se mantém igual quando lida de trás para frente ou de frente para trás, ex ovo.

def verificar_palindromo():
    # Solicita ao usuário que insira uma palavra
    palavra = input("Digite uma palavra: ")

    # Inverte a palavra usando slicing
    palavra_invertida = palavra[::-1]

    # Verifica se a palavra é igual à sua versão invertida
    if palavra == palavra_invertida:
        print(f"A palavra '{palavra}' é um palíndromo!")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")
# Chama a função para executar a verificação de palíndromo
verificar_palindromo()