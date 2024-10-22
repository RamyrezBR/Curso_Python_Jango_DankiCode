'''01 - Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
a) Uma função que receba X e Y como entrada e retorne o maior deles;
b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;
02 - Escreva uma função de potenciação, em que os dados de entrada são: base e
expoente (inteiros).
03 - Crie uma calculadora que consiga executar as funções destacadas da calculadora
padrão do windows 10.'''

import math

# 1º) a) Função maxR retorna o nº maior
def maxR(x,y):
    if x==y:
        return 'Iguais'
    else:
        return max(x,y)

#print(maxR(5,7))


# 1º) b) Função medR retorna a média aritmética dos números
def medR(x,y):
    return (x+y)//2

#print(medR(8,16))


# 2º) Função expoInt retorna o resultado da exponenciação dos números
def expoInt(x,y):
    return x**y

#print(expoInt(2,4))


# 3º) Função calcWin retorna o calculo de ambos os números digitados conforme a operação selecionada 
def calcWin():
    
    print('-_-_-_-_Calculadora do Windows 1.0v-_-_-_-_')
    while True:
        
        opt=int(input('''
            Escolha a operação desejada: 
            
            Soma      -> [1]
            Subtração -> [2]
            Multiplic -> [3]
            Divisão   -> [4]
            Potenc    -> [5]
            Radic     -> [6]
            Fração    -> [7]
            Sair      -> [8]
            
    -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
                    
                    '''))
        if opt==8:
            break
        print('\n-_-_-_Observação-_-_-_: ')
        print('Na operação de radiciação, o primeiro número(x) é a base e o segundo(y), o expoente!')
        x=float(input('\nDigite o 1º número: '))
        y=float(input('\nDigite o 2º número: '))
        
            
        if opt==1:
            print(f'\n{x} + {y} = {x+y}')
        elif opt==2:
            print(f'\n{x} - {y} = {x-y}')
        elif opt==3:
            print(f'\n{x} x {y} = {x*y}')
        elif opt==4:
            print(f'\n{x} / {y} = {x/y}')
        elif opt==5:
            print(f'\n{x} elevado a {y} = {x**y}')
        elif opt==6:
            print(f'\n{x**(1/y)})')
        elif opt==7:
            print(f'\n{1/x}')
        else:
            print('\nERRO!')
        
        
        
    
calcWin()
