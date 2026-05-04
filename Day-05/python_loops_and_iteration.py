fruits = ["Apple", "Peach", "Pear"]        #For Loop(for/in): é um comando que nos possibilita acessar cada item dentro de
                                           #de uma lista individualmente e imprimir um a um
for fruit in fruits:                       #Lembrar de nomear a variável quando usar o comando for/in
    print(fruit)                           #O loop nos permite executar o código que estiver em seu múltiplas vezes
    print(fruit + " pie")                  #dominio
print(fruits)


student_scores = [180, 124, 165, 173, 189, 169, 146]

total_score = sum(student_scores)          #O comando "sum" nos permite somar todos os números dentro de uma lista,
print(total_score)                         #levar em consideração que se tiver alguma str na lista, muito porvavelmente
                                           #dê erro ao executar o comando. Curiosidade:O "sum" é praticamente um
                                           #For Loop criado pela equipe do Python para facilitar nossa vida

soma = 0                                   #Aqui segue um exemplo que podemos fazer a soma dos itens usando o For Loop
for score in student_scores:
    soma += score
print(soma)

#------------------------------------------------- Code Exercise ----------------------------------------------------#
#O desafio consiste em rescreever o comando "max" usando o For Loop

student_scores = [180, 124, 165, 173, 189, 169, 146]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)

#----------------------------------------------------- Part 2 --------------------------------------------------------#
#Range Function

for number in range(1, 10):                    #Com o comando "range()" se quisermos gerar uma "quantia" de números, no
    print(number,)                             #qual conseguimos determinar seu tamanho
print("\n")                                    #Obs: O comando "range()" não funciona sozinho, ele precisa estar
                                               #acompanhado de um For Loop
for number in range(1, 11):                    #Importante lembrar, o ultimo numero por padrão não está incluso, e caso
    print(number,)                             # precise do determinado número lembrar de sempre colocar seu equivalete
print("\n")                                    # a mais, ex: Quero o 10, eu ponho o 11.

for number in range(1, 11, 3):                 #Nesse caso aqui, ao adicionar um terceiro valor aos parentêses do
    print(number)                              #"range()" nos determinos o quão grande sera o intevalo entre os valores
print("\n")                                    #a serem usados
     
#------------------------------------------------- Code Exercise -----------------------------------------------------#    
total = 0
for number in range(1, 101):
    total += number     
print(total)

#--------------------------------------------------- Challenge -------------------------------------------------------#

for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print("FizzBuzz")
    elif number%5 == 0:
        print("Buzz")    
    elif number%3 == 0:
        print("Fizz")
    else:
        print(number)
