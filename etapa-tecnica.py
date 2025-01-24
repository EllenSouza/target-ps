
import random

#questão 1 

indice = 13
soma = 0
k = 0 

while (k < indice):
    k += 1
    soma += k

print("Questão 1")
print(soma)

print("\n\n")

#questão 2

a = -1
b =  1

numero = 13

print("Questão 2")

while (a < numero):
    #fibonacci
    c = a + b
    print(c)
    a = b
    b = c
    #verifica se o número está na sequência
    if (c == numero):
        print("Número está na sequência")
        break


print("\n\n")

#questao 3

print("Questão 3")

#gera valores aleatórios de faturamento entre 100 e 500
faturamento_diario = [random.uniform(100, 500) for _ in range(30)]

menor = min(faturamento_diario)
maior = max(faturamento_diario)

media = sum(faturamento_diario) / len(faturamento_diario)

dias_superior_media = 0

for valor in faturamento_diario:
    if valor > media:
        dias_superior_media += 1

print(f"Menor Faturamento: {menor}\n")
print(f"Maior Faturamento: {maior}\n")

print(f"Dias com faturamento superior a média mensal: {dias_superior_media}\n")


print("\n\n")

#questao 4

print("Questão 4")

faturamento = [
    ("SP", 67836.43),
    ("RJ", 36678.66),
    ("MG", 29229.88),
    ("ES", 27165.48),
    ("Outros", 19849.53)
]
total = 0
for _,valor in faturamento:
    total += valor

for estado, valor in faturamento:
    representacao = (valor / total) * 100
    print( f"{estado}: {representacao:.2f}%")


print("\n\n")

#questao 5
print("Questão 5")

palavra = input("Digite a palavra: ")
inverso = []
#percorre a palavra começando no final
for i in range (len(palavra)-1 , -1, -1):
    inverso.append(palavra[i])

print(''.join(inverso))