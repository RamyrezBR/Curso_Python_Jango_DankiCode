'''01 - Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o
resultado.'''

numbers=[int(input(f'\nDigite o {x+1}º número: '))for x in range(5)]

print(f'\nO maior número é: {max(numbers)}')
print(f'\nO menor número é: {min(numbers)}')