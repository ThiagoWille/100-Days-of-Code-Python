print("Hello"[4])   #O cochete faz com que seja chamado um item específico da String dependendo do número
                    # que se encontra dentro dele. Isso é chamado de "SUBSCRIPTING"
                    #É possível também usar números negativos (-1,-2,etc) fazendo com que o comando seja 
                    # realizado ao contrário

#String
print("123" + "456")    #Como o números estão dentro das aspas, o pc entende que isso é uma string e fará
                        # a concatination por causa do sinal de "+", que é simplesmente juntar uma sentença
                        # a outra, ao invés de somar

#Integer = Whole Number(Número Inteiro)
print(123 + 456)

#Large Integers
print(123_456_789)  #Quando o número for muito grande, adiciona um Underline(_) para facilitar a visuali-
                    #zação do número para nosso olho

#Float = Floating Point Number(Número Decimal)
print(3.14159)

#Boolean(Boleano)
print(True)    #O boleano tras apenas dois valores possíveis, sendo eles, Verdadeiro ou Falso
print(False)

#--------------------------- Part2 ---------------------------------#
print(len("12345"))     #"len" é utilizado apara contar o número de itens dentro do obejeto"()"; e só
                        # funciona com sequências(strings, bytes, tuples, lists e ranges) ou coleções
                        # (dicionários, sets ou frozen sets)

print(type("Hello"))      #"type" é utilizado para descobrir o tipo de qualquer data ou variavél
print(type(12))
print(type(3.5))
print(type(True))

#Type Conversion ou Type Casting
print(int("123") + int("456"))      #É possível fazer a conversão do dado no obejeto, adicionando o
                                    #comando da váriavél, como no exemplo onde temos uma string("123"),
                                    #sendo convertida pelo comando "int", mas tome cuidado que nem tudo
                                    #pode ser convertido, precisa ser algo lógico, como por exemplo, "abc"
                                    #não pode ser transformado em um número
#Desafio Type Conversion
#-- print("Number of letters in your name: " + len(input("Enter your name: "))) --#
# name_user = input("Enter your name:\n")
# name_length = len(name_user)

# print("The number of letters in your name is: " + str(name_length))

#-------------------------- Part3 ---------------------------------#
#Matematical Operators(Operadores Matemáticos)
print(123 + 145)    #Soma
print(7 - 3)        #Subtração
print(3 * 2)        #Multiplicação
print(6 / 3)        #Divisão - Com apenas uma barra ele retorna um valor em Float
print(6 // 3)       #Divisão com "//" - Quando este é usado ele remove o valor decimal do resultado final
                    #oque pode não ser viavél utlizar quando for dividir algum número que não retorne
                    #um número inteiro
print(2 ** 2)       #Potencialização - Ao utilizar dois "**", o pc calcula o 1º número elevado pelo 2º
#OBS: Quando for fazer multiplas operações, tomar cuidado pq, existe uma linha de prioridade:
# Parenteses"()" -> Expoentes"**" -> Multiplicação"*" ou Divisão"/" -> Adição"+" ou Subtração"-"

#---------------------------- Part4 ------------------------------------------#
#Rounding Number(Arredondando os Números)
bmi = 84 / 1.65 **2
print(bmi)              #Esse aqui vai apenas entregar o valor em Float com todos os númeors possiveis
print(int(bmi))     #Esse aqui vai cortar todos os valores após a virgula, ação conhecida como "Flooring"
print(round(bmi))   #Já esse comando leva em considerção os valores após a virgula e arredonda para cima
                    #para baixo dependendo do 1º número após a virgula
print(round(bmi, 2))#Neste caso, ao adicionar um número dentro do "round" após a variável, estamos dizen-
                    #ao computador para deixar a "x" quantidade de números após a virugula no resultado
                    #final

#Assignment Operators
#Nos permite acumular os resultados do nossos cálculos
score = 0
#Se User fez um ponto
score += 1          #Esse comando facilita o codigo, no caso da gente querer somar os numeros gradual-
                    #mente, ao invés de ter que ficar escrevendo "score = score + 1"
score -= 1          #Esse comando subtrai valores do input
score *= 1          #Esse multiplica
score /= 1          #Esse divide

# f-strings
score = 0           #Ao usar um f na frente de uma string(f"x"), temos a possibilidade de adicionar
height = 1.8        #variavéis dentro da string através das "{}" e manter suas características sem que
is_winning = True   #se tornem strings automaticamente

print(f"Your score is: {score}\nYour hight is: {height}\nYou're winning is {is_winning}")