import random                            #Ao importar o modulo "random"(que possui todo o codigo responsável por gerar
                                         #números aleatórios)
                                         #nos possibilita fazer o uso de comandos randomicos

random_integer = random.randint(1, 10) #Ao usar o comando "random.randint()", podemos definir um conjunto
                                       #de números a serem sorteados pelo randomizador e atribuir uma
                                       #variável

import my_module                       #Podemos criar outros modulos também, que facilitem o programa, basta criar outro
                                       # arquivo python, escrever o codigo lá e através do comando "import nome_do_arquivo"
                                       # trazemos a função para o arquivo pricipal


print(my_module.my_fv_number)          #Quando formos fazer uso do modulo, precisamos escrever da seguinte maneira:
                                       #(nome_do_modulo.nome_da_variavel)
                                       #Atenção: Nunca esquecer de usar o ponto entre os dois

rad_numb = random.random() * 10        #O comando "random.random()" trabalha em um range de 0 a 1, mas podemos alterar isso
print(rad_numb)                        #apenas multiplicando o comando, aumentando o range de numeros aleatorios
                                       #Vale lembrar que ele é um "float" e sua estrutura é 0 <= x < 1;
                                       #Conhecido como Semi-Open Range

random_float = random.uniform(1, 10)   #O comando "random.uniform(x, y)" também retorna um float aleatório igual ao anterior
                                       #A diferença com o de cima é que ele tem a capacidade de sortear o segundo numero, já
                                       #que sua estrutura é 0 <= x <= 1

#------------------------------------------------ Desafio Fixação -------------------------------------------------------#
#Escrever um codigo que represente Cara ou Coroa
rand_number = random.randint(1, 2)

if rand_number == 1:
    print("Heads")
else:
    print("Tails")

#-------------------------------------------------------- Part2 ---------------------------------------------------------#
#Lists(Listas)

fruits = ["Melon", "Apple", "Orange"]    #Ao criar uma lista usando "[]", somos capazes de armazenar varias informações em 
                                         #uma única variável; podemos também selecionar um item específico através do número
                                         #equivalente a sua posição, exemplo -> print(fruits[1]), como selecionamos o nº 1,
                                         #vai ser retornado a palavra "Apple" da lista. Vale lembrar que a lista começa do nº 0
print(fruits[1])  

fruits[0] = "Lemon"                      #Podemos manipular as informações que estão dentro de uma lista, como no exemplo ao
                                         #onde reescrevemos o 1º item

fruits.append("Grape")                   #A função X.append() faz com que possamos adicionar uma informação a mais à uma lista
                                         #já criada

fruits.extend(["Watermelon", "etc"])     #Ao utilizar X.extend() é possivél adicionar outra lista, exetendendo a lista
                                         #"principal"

#---------------------------------------------------- Desafio Fixação ---------------------------------------------------#
#Bunker Roulette                           
#1ª Opção                                  
                                           
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

choice = random.randint(0, 4)

print(f"{friends[choice]} will pay the bill!")

#2ª Opção
import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

#-------------------------------------------------------- Part3 ---------------------------------------------------------#
fruits = ["Strawberry", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
                                               
dirty_dozen = [fruits, vegetables]             #É possível colocar listas dentro de outra lista, isso se chama Nesting Lists
                                               #Lembrar que em uma nested list, a primeira lista é 0, seguindo a mesma lógica
                                               #de uma lista padrão, onde o primeiro indice começa do 0