print("Welcome to the rollercoaster!")                  #Qunado for necessário fazer comparações normalmente a gente usa o "if" acompanhado de "else",
                                                        #onde basicamente o "if" testa se a variável é verdadeira e executa o comando e caso seja
height = int(input("What is your height in cm?\n"))     #seja Falsa, executa o comando contido no "else"
bill = 0                                                #O "elif" nos proporciona adicionar mais de uma condição dentro do "if/else"
                                                        #Operadores de Comparação
if height >= 120:                                       # > - Greater Than(Maior Que)
    print("You can ride the rollercoaster")             # < - Less Than(Menor Que)
    age = int(input("What is your age?\n"))               # >= - Greater Than or Equal To(Maior ou Igual)
    if age <= 12:                                       # <= - Less Than or Equal To(Menor ou Igual)
        bill = 5                                        # == - Equal to(Igual) OBS:Para comparar precisa usar esse, pq o "=" isolado atribui valores
        print("Child tickets are $5!")                  # != - Not equal to(Diferete)
    elif age <= 18:                                     
        bill = 7                                                
        print("Youth tickets are $7!")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You can ride for free")                 
    else:
        bill = 12
        print("Adult tickets are $12!")

    wants_photo = input("Do you want a photo take? Type y for Yes and n for No.\n") 
    if wants_photo == "y":
        bill += 3
    
    print(f"Your final Bill is: ${bill}")

else:                                                   
    print("You must be taller to be able to ride!")                    

# #Operador MODULO
print(10 % 5)                  #Ele faz uma divisão, no caso de não ter sobra no cálculo ele retorna o valor de 0
print(20 % 9)                  #Agora se a divisão tiver sobra, ele retorna o valor que sobrou do cálculo

# #Desafio de Fixação
print("Welcome to the Odd/Even Checker!")

number = int(input("What number do you want to check?\n"))

number_check = number % 2

if number_check == 0:
    print("This is a Even number!")
else:
    print("This is a Odd number!")


#--------------------------------------------------- Challenge ---------------------------------------------------#
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L:\n")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input ("Do you want extra cheese? Y or N:\n")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
   print("Invalid Option!")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final Bill is: ${bill}")

#-------------------------------------------------- Challenge.V2 --------------------------------------------------#
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L:\n").upper()
bill = 0
if size in ["S", "M", "L"]:
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    elif size == "L":
        bill = 25

    pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n").upper()
    if pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    extra_cheese = input ("Do you want extra cheese? Y or N:\n").upper()
    if extra_cheese == "Y":
        bill += 1


    print(f"Your final Bill is: ${bill}")
else:
   print("Invalid Option!")

#-----------------------------------------------------------------------------------------------------------------#
#Logical Operators(Operadores Lógicos)
A = 1
B = 1

A and B     #Operador AND: As duas variavéis precisam ser verdadeiras para retornarem "True", se uma delas for falsa o resultado é "False"
A or B      #Operador OR: Uma ou as duas sendo verdade retorna "True" e só retorna "False" quando as duas forem Falsas
not A       #Operador NOT: Inverte o resultado, oque é verdadeiro retorna "False" e oque é falso retonra "True"