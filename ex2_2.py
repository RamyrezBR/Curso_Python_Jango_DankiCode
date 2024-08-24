'''01 - Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
acordo com os critérios:

● Menor de 16 anos: MENOR
● Entre 16 e 18 anos: EMANCIPADO
● Maior de 18 anos: MAIOR'''

idade=int(input("\nDigite a idade da pessoa: ").strip())
if (idade >= 18):
    print(f'\nA pessoa com {idade} anos é considerada MAIOR!')
elif (idade >= 16 and idade < 18):
    print(f'\nA pessoa com {idade} anos é considerada EMANCIPADA!')
else:
    print(f'\nA pessoa com {idade} anos é considerada MENOR!')

'''02 - Implemente um programa que receba a idade de um nadador e imprima a sua
categoria seguindo as regras: 
                            
                            Infantil A: 5-7
                            Infantil B: 8-10
                            Juvenil A:  11-13
                            Juvenil B:  14-17'''

idade=int(input("\nDigite a idade do nadador: ").strip())
if (idade >= 14 and idade <= 17):
    print(f'\nO nadador com {idade} anos é considerado JUVENIL B!')
elif (idade >= 11 and idade <= 13):
    print(f'\nO nadador com {idade} anos é considerado JUVENIL A!')
elif (idade >= 8 and idade <= 10):
    print(f'\nO nadador com {idade} anos é considerado INFANTIL B!')
elif (idade >= 5 and idade <= 7):
    print(f'\nO nadador com {idade} anos é considerado INFANTIL A!')
else:
    print(f'\nA idade digitada não corresponde a nenhuma das categorias disponíveis!')
    
