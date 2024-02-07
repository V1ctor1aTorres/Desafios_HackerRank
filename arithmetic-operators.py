"""O código deve ler 2 númerosinteiros 'a' e 'b' 
e imprimir 3 linhas de código  contendo:
-A soma dos 2 numeros
-A diferença dos 2 números
-O produto dos 2 números
Restrição: 
-1<=a<=10**10
-1<=b<=10**10"""

#Pega 2 números do usuário remove os espaços em branco
#E guarda nas variáveis 'a' e 'b'
a = int(input().strip())
b = int(input().strip())
#Se 'a' e 'b' estiverem entre 1 e 10**10
if 1 <= a <= 10**10 and 1 <= b <= 10**10:
    #Escreva a soma
    print(a+b)
    #Escreva a diferença
    print(a-b)
    #Escreva o produto
    print(a*b)

