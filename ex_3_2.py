'''02 - Escreva um programa para calcular as somas:
S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)
S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)'''


# PRIMEIRA SOMA: S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1

print('-_'*30)
print('RESULTADO DA PRIMEIRA SOMA:')
s1=(3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1)
print(f'\n{s1}')

# SEGUNDA SOMA: S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25 + (20 primeiros termos)

print('-_'*30)
print('RESULTADO DA SEGUNDA SOMA:')
n2,d2,s2=460,25,0

for i in range(20):
    n2-=5
    d2+=1
    print(f'\n{i+1}º termo: {n2}/{d2} +')
    s2+=(n2/d2)

s2+=(480/2 + 475/22 + 470/23 + 465/24 + 460/25)
print(f'\n{s2}')

# TERCEIRA SOMA: S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29 + (15 primeiros termos)

print('-_'*30)
print('RESULTADO DA TERCEIRA SOMA:')
n3,d3,s3=31,29,0

for i in range(15):
    n3+=n3+1
    d3+=2
    print(f'\n{i+1}º termo: {n3}/{d3} +')
    s3+=(n3/d3)

s3+=(1/2 + 3/23 + 7/25 + 15/27 + 31/29)
print(f'\n{s3}')