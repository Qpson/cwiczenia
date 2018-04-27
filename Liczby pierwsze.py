def liczbyPierwsze(dolnaGranica, gornaGranica):
    print("Liczby pierwsze od ",dolnaGranica,"do",gornaGranica,"to:")
    for liczba in range(dolnaGranica,gornaGranica + 1):
        if liczba> 1:
            for i in range(2,liczba):
                if (liczba % i) == 0:
                    break
            else:
                print(liczba)

def main():
    dolnaGranica = int(input('Podaj pierwsza liczbe, od jakiej chcesz sprawdzac: '))
    gornaGranica = int(input('Podaj ostatnia liczbe, do ktorej chcesz sprawdzac: '))
    print(liczbyPierwsze(dolnaGranica, gornaGranica))

main()
