# FizzBuzz é um jogo de programação simples e clássico, frequentemente usado para ensinar lógica básica e fluxo de
# controle. O jogo envolve iterar através de números de 1 até um limite especificado. Para cada número:

# Se o número for divisível por 3, o programa exibe "Fizz."
# Se o número for divisível por 7, ele exibe "Buzz."
# Se o número for divisível por ambos 3 e 7, ele exibe "FizzBuzz."
# Caso contrário, ele simplesmente exibe o número.
# Números que contêm o dígito "3", mas não são divisíveis por 3 ou 7, devem retornar Almost Fizz


def fizzbuzz(number: int):
    if number % 3 == 0 and number % 7 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 7 == 0:
        return "Buzz"
    if "3" in str(number):
        return "Almost Fizz"

    return str(number)


print("Welcome to FizzBuzz!")

entry = int(input("Insert your number"))

for i in range(1, entry + 1):
    print(fizzbuzz(i))
