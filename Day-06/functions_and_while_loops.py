print()                         #Funções são basicamente um nome que retem um bloco de código, e para reconhecer uma
                                #é só observar se  tem um nome acompanhado por parênteses, ex: print(), len(), max()
                                #O time de desenvolvedores do Python já nos disponibiliza uma vasta lista de funções
                                #que podemos usar, mas isso não nos impossibilita de criar nossas própias
                                #Link: https://docs.python.org/3/library/functions.html

def my_function():              #Ao usar "def" e em seguida por um "nome():" estamos criando/definindo uma nova função,
    print("Hello")              # e todo código indentado será utilizado ao chama pela função posteriormente
    print("Bye")

my_function()                   #Ao especificar o nome com parênteses, nós estamos chamando a função(Calling Function)

#--------------------------------------------------- Part2 -----------------------------------------------------------#
#while something_is_true:       #O "while Loop" rodará o código indentado enquanto a sentença for verdadeira
                                #Ele testará a sentença até que retorne "False" para poder parar o loop