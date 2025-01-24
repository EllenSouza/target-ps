#questão 1 

indice = 13
soma = 0
k = 0 

while (k < indice):
    k += 1
    soma += k

print("Questão 1")
print(soma)


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

#questao 5
print("Questão 5")

palavra = input("Digite a palavra: ")
inverso = []
#percorre a palavra começando no final
for i in range (len(palavra)-1 , -1, -1):
    inverso.append(palavra[i])

print(''.join(inverso))