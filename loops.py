"""O código deve ler um número inteiro n
para todos os inteiros não negativos 
i<n, escreva i**2"""

#Pega o input do usuário retira os espaços em branco
#e guarda na variável 'n'
n = int(input().strip())
#Se 'n' estiver entre 1 e 20
if 1 <= n <= 20:
    #Para cada índice no range de 0 à 'n'
    for i in range(0, n):
        #Escreva o índice elevado a 2
        print(i**2)
