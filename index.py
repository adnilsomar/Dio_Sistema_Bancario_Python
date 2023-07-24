balance = 0
limit = 500
extract = ""
withdraw_number = 0
WITHDRAW_LIMIT = 3
withdraw_sum = 0

while True:
    option = input(f'''
Por favor, selecione uma das opções:
[1]Depósito
[2]Saque
[3]extrato
[4]Sair

''')

    if option == '1':
        deposit = float(input('Por favor, inserir o valor que deseja depositar: '))
        if deposit <= 0:
            print('Operação falou! O valor informado é inválido.')
        else:
            balance += deposit
            print(f'Operação realizada com sucesso. Seu saldo atual é R$ {balance:.2f}\n')
            extract += f'Deposito: R$ {deposit:.2f}\n'
            deposit_option = input(f'''Por favor, selecione uma das siguintes opções: 
                  [1] Para voltar para o menu anterior
                  [2] Para sair
                                   
                  ''')
            if deposit_option =="2":
             break

    elif option == '2':
        
        if withdraw_number >= 3:
          print('Operação falhou! Número máximo de saques excedido.')
        elif withdraw_sum == 500:
          print('Operação falhou! Máximo valor de saque diário atingido.')
        else:
          withdraw = float(input('Por favor, inserir o valor que deseja sacar: '))
          if balance < withdraw :
            print('Operação falhou! Você não tem saldo suficiente.')
          elif (withdraw + withdraw_sum)>500:
             print('Operação falhou! O valor inserido ultrapassa o límite de saque diáçrio.')
          elif(balance > withdraw):
             balance -= withdraw
             withdraw_number += 1
             withdraw_sum += withdraw
             extract += f'Saque: R$ {withdraw}\n'
             print(f'Saque realizado com sucesso.')
          else:
            print('Operação falhou! Valor inserido inválido.')
        
    elif option == '3':
        print('********EXTRATO********\n')
        print('Não foram realizadas movimentações.' if not extract else extract)
        print(f'\nSaldo R$ {balance:.2f}\n')
        print('**********************\n')
    elif option == '4':
        print ('')
        break
    else:
        print('Operación inválida, por favor selecione novamente a opção desejada')
  
    
