valor = int(input())
print(valor)
print(int(valor/100), "nota(s) de R$ 100,00")
valor=valor%100
print(int(valor/50), "nota(s) de R$ 50,00")
valor=valor%50
print(int(valor/20), "nota(s) de R$ 20,00")
valor=valor%20
print(int(valor/10), "nota(s) de R$ 10,00")
valor=valor%10
print(int(valor/5), "nota(s) de R$ 5,00")
valor=valor%5
print(int(valor/2), "nota(s) de R$ 2,00")
valor=valor%2
print(int(valor/1), "nota(s) de R$ 1,00")
valor=valor%1
