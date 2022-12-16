def add_numbers(first, second):
    return first + second


def subtraction_numbers(first, second):
    return first - second


def multiplication_numbers(first, second):
    return first * second


def sharing_numbers(first, second):
    if second == 0:
        print("Nie dziel przez 0")
        return

    return first / second


def compounding_numbers(first, second):
    return first ** second


def pierwiastkowanie(first, second):
    if second % 2 == 0 and first < 0:
        print("nie można wykonywać takiego działanai")
        return
    return first ** (1 / second)


def off(first, second):
    raise NotImplemented("Wyłączenie kalkulatora")


def get_first_number():
    print("wpisz pierwszą liczbę")
    while True:
        try:
            first = float(input())
            return first
        except ValueError:
            print("Podaj niepoprawną wartość")


def get_second_number():
    print("wpisz druga liczbę")
    while True:
        try:
            first = float(input())
            return first
        except ValueError:
            print("Podaj niepoprawną wartość")




choose_type_calculation_function = {
    1: add_numbers,
    2: subtraction_numbers,
    3: multiplication_numbers,
    4: sharing_numbers,
    5: compounding_numbers,
    6: pierwiastkowanie,
}
choose_type_calculation_function_names = {
    1: "1.suma",
    2: "2.odejmowanie",
    3: "3.mnożenie",
    4: "4.dzielenie",
    5: "5.potęgowanie",
    6: "6.pierwiastkowanie",
}

for litera in choose_type_calculation_function_names.values():
    print(litera)

print("""wybierz rodzaj działania :
             1.dodawanie
             2.odejmowanie
             3.mnożenie
             4.dzielenie
             5.potęgowanie
             6.pierwiastkowanie
             7.wyłączeni""")