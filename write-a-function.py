"""
Escreva a lógica para uma função que diz qual ano é bissexto.
As condições são:
-Se o ano é divisivel por 4 então é bissexto, a menos que
- O ano seja divisivel por 100, então não é bissexto, a menos que 
-O ano também é divisivel por 400. Então é bissexto.
Restrição: 1900<= year<=10**5
"""

#Função
def is_leap(year):
    #Se o ano estiver entre 1900 e 10**5
    if 1900 <= year <= 10**5:
        #Se ano é divisivel por 4 e não é por 100
        #OU
        #Se o ano é divisivel por 4 e por 400
        if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
            #É bissexto
            leap = True
        else:
            #Não é bissexto
            leap = False
    #Retorna o valor True/False
    return leap
    
    
year = int(input())
print(is_leap(year))
