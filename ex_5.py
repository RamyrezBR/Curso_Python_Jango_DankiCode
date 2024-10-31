'''
1. Documentação da função calcWin
    1.1 A função calcWin consiste em simular uma calculadora do windows com algumas operações básicas
    1.2 Como a função não exige parâmetros, não há necessidade de inserir nenhum dado no chamamento da função
'''


def calcWin():
    '''
    1.1a A função é iniciada com o loop do tipo while no qual permite que o menu seja exibido ao final de cada operação, a menos que o usuário selecione a opção sair[8]
    1.1b Conforme o menu de opções, as operações disponíveis estão numeradas de 1 a 7 e o nº 8 para sair do programa. Por outro lado, se o usuário digitar algum dado incompatível, será exibida uma mensagem de erro e o usuário será redirecionado ao menu de operações
    '''
    
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
