import numpy as np
import requests
# Excercício 2 sobre Estruturas Lógicas e Condicionais

# 2.1 - Área de um retângulo

print("\n1: Calcule a área de um retângulo:\n")
base=float(input("Defina a base: ").strip())
altura=float(input("\nDefina a altura: ").strip())
print(f"\nA área do seu retângulo é: {base*altura} cm²")

# 2.2 - Área de um quadrado

print("\n2: Calcule a área de um quadrado:\n")
base=float(input("Defina a base: ").strip())
altura=float(input("\nDefina a altura: ").strip())
print(f"\nA área do seu quadrado é: {base*altura} cm²")

# 2.3 - Valor de determinado produto com uma porcentagem de desconto

print("\n3: Calcule a valor de um produto:\n")
valor=float(input("Defina o valor do produto: ").strip())
desconto=float(input("\nDefina o valor do desconto %: ").strip())
print(f"\nO valor do produto com desconto é: R$ {valor-(valor*desconto/100):.2f}")

# 2.4 - Área de um círculo

print("\n4: Calcule a área de um circulo:\n")
base=float(input("Defina o raio: ").strip())
print(f"\nA área do seu círculo é: {base*np.pi:.2f} cm²")

# 2.5 - Conversão em reais para dólar
# Consumi uma api de câmbio para tornar o projeto mais dinâmico

url='https://economia.awesomeapi.com.br/json/last/USD-BRL'

response=requests.get(url)
if response.status_code==200:
    dados=response.json()
    result=dados["USDBRL"]
    valor=result['bid']
else:
    print(f'{response.status_code}')

print("\n5: Calcule o valor Dolar em R$:\n")
reais=float(input("Defina o valor em Dolar: $").strip())
print(f"\nO valor convertido em Reais é: R$ {float(valor)*reais:.2f}")
