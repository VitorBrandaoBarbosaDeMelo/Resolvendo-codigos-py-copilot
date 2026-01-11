# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

def repetir_texto():
    # Solicitar o texto do usuário
    texto = input("Digite o texto que deseja repetir: ")

    # Repetir o texto 5 vezes
    for _ in range(5):
        print(texto)

# Chamar a função
repetir_texto()
