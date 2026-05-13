def greet():
    print("Hello User")
    print("Good day")
    print("Prepared for another run?")

greet()

#Functions that allows for input

def greet_with_name(name):               #Ao definir uma função e alocar uma variável dentro dos parênteses,
    print(f"Hello {name}")               #ao chamarmos a função ela ira aguardar um input para que possa ro-
    print(f"How do you do {name}?")      #dar o código contindo em si
                                         #A informação que passamos se iguala à variável dentro dos "()" da
greet_with_name("Thiago")                #função, são denomidadas como Parametro(Var-Função) = Argumento(Var_IN)

#Function with more than 1 input

def greet_with(name, location):            #Podemos adicionar inumeras entradas na função, mas vale lembrar que
    print(f"Hello {name}")                 #ela funciona em ordem crescente, oque pode ocasionar erro em sua ex-
    print(f"What is like in {location}?")  #caso dados sejam alocados de maneira errada

greet_with("Jack", "Oblivion")            
greet_with(location="Nowhere", name="Jack") #Para contornar isso podemos usar "Keywords Arguments", oque é basi-
                                            #camente igualar o argumento ao seu parametro correto





