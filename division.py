"""O código deve ler 2 números inteiros,
adicionando lógica deve  imprimir 2 linhas contendo:
-A parte inteira da divisão a//b
-Divisão exata a/b"""

#Pega o input do usuário remove os espaços em branco
#e guarda nas variáveis 'a' e 'b'
a = int(input().strip())
b = int(input().strip())
#Mostra a parte inteira da divisão
print(a//b)
#Mostra a divisão exata
print(a/b)