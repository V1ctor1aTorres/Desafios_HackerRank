"""O código deve ler um número inteiro e sem usar strings
tente escrever '1...n' mostrando os valores consecultivos entre 1 e 'n'
"""

#Recebe um input do usuário, retira os espaços em branco
#e guarda na variável 'n'
n = int(input().strip())
#Se 'n' estiver entre 1 e 150
if 1 <= n <= 150:
    #Para cada índice no range de 1 até 'n'
    for i in range(1, n+1):
        #Escreva os valores consecultivos
        print(i, end="")
    
