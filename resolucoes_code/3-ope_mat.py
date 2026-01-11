# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
def somar_matriz():
    # Solicitar as dimensões da matriz
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))

    # Criar a matriz vazia
    matriz = []

    # Preencher a matriz com valores
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            valor = int(input(f"Digite o valor para a posição [{_}][{__}]: "))
            linha.append(valor)
        matriz.append(linha)

    # Somar os elementos da matriz
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento

    # Exibir a soma dos elementos
    print("Soma dos elementos da matriz:", soma)

# Chamar a função
somar_matriz()
