"""Você deve garantir que o primeiro e o ultimo nome de uma pessoa
comecem com letra maiusculas. Dado um nome completo 
sua tarefa é capitalizar corretamente.
Restrições:
-0<len(s)<1000
-A string deve consistir em caracteres alfanumericos  e espaços"""

#Função para capitalizar
def solve(s):
    # A função split(" ") divide a string 
    #sempre que encontra um espaço em branco e retorna uma lista das partes resultantes.
    #A lista resultante é atribuída à variável name
    name = s.split(" ")
    # Inicializa uma string vazia chamada k. 
    #Essa variável será usada para armazenar a versão modificada da string original.
    k = ""
    #Inicia um loop que itera sobre cada elemento da lista name
    for x in name:
        #Converte o primeiro caractere de x para maiúsculo usando o método capitalize()
        #Em seguida, concatena essa versão modificada de x com a string k, 
        #seguida por um espaço em branco.
        k += x.capitalize() + " "
        #Retorna a string final k
    return k