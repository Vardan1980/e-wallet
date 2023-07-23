import datetime
balance = 250
password = '1234'
name = 'Joe'
attempts = 0
status = False
today_cashIn = 0
today_cashOut = 0
lastProccess = 'today no proccess'
while True:
    if status:
        break
    if attempts == 3:
        print('Card Blocked !')
        break
    passw = input('Enter your password >>>')
    if passw == password:
        print(f'Welcome Dear {name} !!!')
        print('-'*20)
        print('Balance >>> b')
        print('Cash In >>> +')
        print('Cash Out >>> -')
        print('Print check >>> p')
        print('Day history >>> h')
        print('Exit >>> e')
        print('-'*20)
        while True:
            command = input('Print your command >>>')
            if command == 'b':
                print('-'*20)
                print(f'Dear {name} your balance: >>> {balance} $ !!!')
                print('-'*20)
                continue
            elif command == '+':
                sum = int(input('Print sum >>>'))
                balance += sum
                today_cashIn += sum
                lastProccess = datetime.datetime.now()
                print(f'Dear {name} your balance check in {sum} $ !!!')
                continue
            elif command == '-':
                while True:
                    sum = int(input('Print sum >>>'))
                    if sum > balance:
                        print(f'Dear {Joe} do not have in balance {sum} $ !!!')
                        print('Error, try again !')
                        continue
                    else:
                        balance -= sum
                        today_cashOut += sum
                        lastProccess = datetime.datetime.now()
                        print(f'Dear {name} your balance check out {sum} $ !!!')
                        break
                    continue
            elif command == 'e':
                print(f'By Dear {name} !!!')
                print('Exit')
                status = True
                break
            elif command == 'p':
                print('-'*20)
                print(f'Dear {name} it`s your check !!!')
                print(f'Balance:  {balance} $')
                print(f'Date:  {datetime.datetime.now()}')
                print('-'*20)
                continue
            elif command == 'h':
                print('-'*20)
                print(f'Dear  {name} it`s your today history !!!')
                print(f'Balance:  {balance} $')
                print(f'Cash In:  {today_cashIn} $')
                print(f'Cash Out:  {today_cashOut} $')
                print(f'Date:  {datetime.date.today()}')
                print(f'Last Proccess:  {lastProccess}')
                print('-'*20)
            else:
                print('Bad command')
    else:
        print('Wrong password ! , try again !!!')
        attempts += 1
        continue