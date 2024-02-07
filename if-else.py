"""Desafio:
Dado um número inteiro 'n', seguindo as condições:
-Se n é impar, escreva 'Weird'
-Se n é par e está entre 2 e 5, escreva 'Not Weird'
-Se n é par e está entre 6 e 20, escreva 'Weird'
-Se n é par e maior que 20, escreva 'Not Weird'
-Restrição: 1<=n<=100
"""

#Pega o input do usuário retira os espaços em branco 
#e guarda na variável n
n = int(input().strip())
#Se n entiver entre 1 e 100
if 1 <= n <= 100:
    #Se n for par
    if n % 2 == 0:
        #Se n entiver entre 2 e 5 ou for maior que 20
        if 2 <= n <= 5 or n > 20:
            print('Not Weird')
        #Se n estiver entre 6 e 20
        elif 6 <= n <= 20:
            print('Weird')
    #Se n for impar
    else:
        print('Weird')
