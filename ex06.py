#Exercício 6 - Ler temperatura em graus Celsius e converter para Fahrenheit
print('Escolha a temperatura em graus Celsius:')
c = float(input())
f = round((c*(9.0/5.0)+32.0),1)

print(f'Neste momento {f} graus Fahrenheit')