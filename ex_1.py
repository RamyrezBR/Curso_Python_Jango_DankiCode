'''Crie um código com todas as variáveis necessárias
para imprimir utilizando a função print ("Lembre-se que deve ser possível trocar nomes,
preços e dados apenas alterando os valores das variáveis"):

Situação 01 - Gabriel é o cliente de uma livraria online que acaba
de comprar 01 livro com o título lógica de programação por R$79,30
o vendedor Marcos recebeu uma comissão de R$30,00 pela venda.

Situação 02 - A autora (Beatriz) publicou um post em um blog'''


print("\n-_-_Situação nº 1-_-_\n")

nome_Cliente=str(input("\nNome do Cliente: "))
nome_Comissionado=str(input("\nNome do Comissionado: "))
nome_Livro=str(input("\nNome do Livro: "))
valor_Livro=float(input("\nValor do Livro: "))
qtd=int(input("\nQuantidade a ser comprada: "))


print(f'''\nOlá, {nome_Cliente} sua compra de {qtd} livro(s) 
"{nome_Livro}" por R$ {valor_Livro*qtd} foi efetuada com sucesso!".

"Olá, {nome_Comissionado} você acaba de receber uma comissão de R$ {(valor_Livro*qtd)*0.3} 
pela compra realizada pelo(a) cliente {nome_Cliente}\n''')

print("\n-_-_Situação nº 2-_-_\n")

nome_Auth=str(input("\nNome do Autor: "))
titulo_Post=str(input("\nTítulo do post: "))
shares=int(input("\nQtd de compartilhamentos: "))

print(f'''\n{nome_Auth}, seu post com o título "{titulo_Post}" gerou {shares}
compartilhamentos\n''')
