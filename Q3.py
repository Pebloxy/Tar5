a = 0
b = 0
c = 0

print ("Bem-Vindo a calculadora de triângulos")
while True:
    a = int (input ("\nDigite o primeiro número: "))
    b = int (input ("Digite o segundo número: "))
    c = int (input ("Digite o terceiro número: "))
    if ( a >= (b + c) or b >= (a + c) or c >= (b + a) ):
        print("\nNão é um triângulo!")
    else:
        if (a == b and a == c and b == c):
            print("\nÉ um triângulo equilátero")
        elif (a != b and a != c and b != c):
            print("\nÉ um triângulo escaleno")
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("\nÉ um triângulo isósceles")
        else:
            print("Que?")
        break