def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return num1 / num2

print("Calculadora Simples em Python")
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == '1':
    print(f"O resultado é: {somar(num1, num2)}")
elif escolha == '2':
    print(f"O resultado é: {subtrair(num1, num2)}")
elif escolha == '3':
    print(f"O resultado é: {multiplicar(num1, num2)}")
elif escolha == '4':
    print(f"O resultado é: {dividir(num1, num2)}")
else:
    print("Escolha inválida.")
