dolnaGranica = int(input('Podaj od jakiej liczby sprawdzac: '))
gornaGranica = int(input('Podaj do jakiej liczby sprawdzac: '))



print("Liczby pierwsze zaczynajac od " ,dolnaGranica, "do" ,gornaGranica, "to:")

for liczba in range(dolnaGranica, gornaGranica + 1):
   if liczba> 1:
       for i in range(2,liczba):
           if (liczba % i) == 0:
               break
       else:
           print(liczba)
