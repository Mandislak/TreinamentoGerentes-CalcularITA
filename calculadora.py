# CalcularITA

def multiplicacao(a, b):
    return a * b
def divisao(a, b):
    if(b == 0):
        print("Erro, divisão por zero!")
        return None
    else:
        return a / b

#Teste das funções
if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print("Multiplicação:", multiplicacao(num1, num2))
    print("Divisão:", divisao(num1, num2))