#Exercício 7 - Ler temperatura em graus Fahrenheit e converter para Celsius
print('Digite a temperatura em graus Fahrenheit:')
f = float(input())
c = round((5.0*(f-32.0)/9.0),1)

print(f'Neste momento {c} graus Celsius')