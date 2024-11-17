'''Exercício:
01 - Criar um módulo em python capaz de registrar dados de pacientes.
Dados: nome completo, e-mail, cpf, rg, telefone, data de nascimento
Atenção: Seu código deve ser capaz de calcular a idade do paciente. Em caso da idade ser maior ou igual a 65 anos, este paciente deve ter seus dados salvos em um arquivo com a informação que este paciente é do grupo de risco. Caso o paciente tenha idade menor que 65, os dados deste paciente devem ser registrados no mesmo arquivo sem a informação do grupo de risco. Ao final do código, o programa deve imprimir todos os pacientes e solicitar uma confirmação para registrar um novo paciente no arquivo.
# Não se esqueça de implementar o if __name__ == '__main__':
'''


import os
from datetime import datetime


def pacient_creator():
    global idade
    
    while True:
        
        paciente={}
        try:
            paciente["nome"] = input("Digite o nome do paciente: ")
            paciente["email"] = input("Digite o email do paciente: ")
            paciente["cpf"] = input("Digite o CPF do paciente: ")
            paciente["rg"] = input("Digite o RG do paciente: ")
            paciente["telefone"] = input("Digite o telefone do paciente: ")
            paciente["data_nascimento"] = str(input("Digite a data de nascimento (dd/mm/aaaa): "))
            paciente["Grupo de Risco"]="NÃO"
        
            data_nascimento_str=paciente["data_nascimento"]
            data_nascimento=datetime.strptime(data_nascimento_str, "%d/%m/%Y")
            idade=datetime.now().year-data_nascimento.year

            if idade>=65:
                paciente["Grupo de Risco"]="SIM"
            
            return paciente
        
        except ValueError:
            print('Formato inválido!')


def file_creator():
    while True:
        pacientes=[]
        inst_creator=pacient_creator()
        pacientes.append(inst_creator)
    
        with open('lista.txt','a') as paciente:
        
            for i in pacientes:
                paciente.write(f"Nome: {i['nome']}\n")
                paciente.write(f"Email: {i['email']}\n")
                paciente.write(f"CPF: {i['cpf']}\n")
                paciente.write(f"RG: {i['rg']}\n")
                paciente.write(f"Telefone: {i['telefone']}\n")
                paciente.write(f"Data de Nascimento: {i['data_nascimento']}\n")
                paciente.write(f"Grupo de Risco: {i['Grupo de Risco']} ({idade} anos)\n")
                paciente.write("-" * 30 + "\n")
        
        
        opc=int(input('\nAdicionar outro paciente? Sim: [1] Não: [0]'))
        if opc==0:
            break
        else:
            pass


with open('lista.txt','a') as paciente:
        paciente.write("Lista de Pacientes\n")
        paciente.write("=" * 30 + "\n")

if __name__ == '__main__':
    file_creator()
    



