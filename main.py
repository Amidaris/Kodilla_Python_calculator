import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

def calculator(): 
    print("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    operation = int(input())

    number_01 = float(input("Podaj składnik 1: "))
    number_02 = float(input("Podaj składnik 2: "))

    if operation == 1:
        logging.info(f"Dodaję {number_01} i {number_02}")
        print(f"Wynik to {number_01 + number_02}")
    elif operation == 2:
        logging.info(f"Odejmuję {number_01} i {number_02}")
        print(f"Wynik to {number_01 - number_02}")
    elif operation == 3:
        logging.info(f"Mnożę {number_01} i {number_02}")
        print(f"Wynik to {number_01 * number_02}")
    elif operation == 4:
        logging.info(f"Dzielę {number_01} i {number_02}")
        print(f"Wynik to {number_01 / number_02}")
    else:
        print("Niepoprawny wybór działania.")

if __name__ == "__main__":
    calculator()
