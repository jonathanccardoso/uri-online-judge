nome=input()
salario=float(input())
valor_vendido=float(input())
operacao=(valor_vendido * (15/100)) + salario
print("TOTAL = R$", "{0:.2f}". format(operacao))
