#valores maior e menor.
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
maior = n1
menor = n2
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3
print("O maior valor é : {}".format(maior))
print("O menor valor é : {}".format(menor))