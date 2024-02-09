"""Foram dados dois nomes de uma pessoa. 
Sua tarefa é ler esse nomes e escrevê-los no seguinte formato:
'Hello firstname lastname! You just delved  into python.'
Complete a função print_full_name no editor,
com os seguintes paramêtros:
- string first: primeiro nome
- string last: ultimo nome
Restrição: o tamanho de first e last deve ser <=10"""

#Função que vai escrever a frase
def print_full_name(first, last):
    #Se o tamanho do parâmetro for menor ou igual a 10
    if len(first_name) <= 10 and len(last_name) <= 10:
        #Escreva a frase
        print('Hello {} {}! You just delved into python.'.format(first_name, last_name))

if __name__ == '__main__':
    #Lê o input para o primeiro nome
    first_name = input()
    #Lê o input para o segundo nome
    last_name = input()
    #Chama a função
    print_full_name(first_name, last_name)