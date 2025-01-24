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




#questao 5
print("Questão 5")

palavra = input("Digite a palavra: ")
inverso = []
#percorre a palavra começando no final
for i in range (len(palavra)-1 , -1, -1):
    inverso.append(palavra[i])

print(''.join(inverso))