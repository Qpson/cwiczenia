while True:
    piwerko = input('Czy napiłbyś się piwerka?').lower()
    if piwerko == 'tak':
        while True:
            dowodzik = input('A dowodzik to posiadamy?').lower()
            if dowodzik == 'tak':
                print('To zapraszam.')
            elif dowodzik == 'nie':
                print('Ić stont!')
            else:
                print('Legitymacja szkolna się nie liczy.')
            break
    elif piwerko == 'nie':
        print('Ta, na pewno.')
    else:
        print('Już chyba parę zostało wypitych.')
   
