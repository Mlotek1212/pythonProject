from calculator.show_info import print_available_function_by_list


def get_type_of_calculation():
    is_ok = False

    print_available_function_by_list()
    while not is_ok:
        try:
            type_calculation = int(input())
            if type_calculation > 7 or type_calculation < 1:
                print("Podałeś błędną liczbę sprubój jeszcze raz")


            else:
                is_ok = True


        except ValueError:
            print("Wpisałeś litere ")
    return type_calculation



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



def main1(first_number):
    type_calculation = get_type_of_calculation()
    second_number = get_second_number()
    result = None
    if type_calculation == 1:
        result = add_numbers(first_number, second_number)

    elif type_calculation == 2:
        result = subtraction_numbers(first_number, second_number)

    elif type_calculation == 3:
        result = multiplication_numbers(first_number, second_number)

    elif type_calculation == 4:
        result = sharing_numbers(first_number, second_number)

    elif type_calculation == 5:
        result = compounding_numbers(first_number, second_number)

    elif type_calculation == 6:
        result = pierwiastkowanie(first_number, second_number)

    elif type_calculation == 7:
        raise NotImplemented("Wyłączenie kalkulatora")
    print(result)
    return result


def main2(first_number):
    type_calculation = get_type_of_calculation()
    second_number = get_second_number()
    choose_function = None
    if type_calculation == 1:
        choose_function = add_numbers
    elif type_calculation == 2:
        choose_function = subtraction_numbers
    elif type_calculation == 3:
        choose_function = multiplication_numbers
    elif type_calculation == 4:
        choose_function = sharing_numbers
    elif type_calculation == 5:
        choose_function = compounding_numbers
    elif type_calculation == 6:
        choose_function = pierwiastkowanie
    result = choose_function(first_number, second_number)
    print(result)
    return result


def main3(first_number):
    type_calculation = get_type_of_calculation()
    if type_calculation == 7:
        raise
    second_number = get_second_number()
    # g = {"2": "two"}
    # g["sf"] -> wyjątek
    # g.get("2", "brak") -> "two"
    # g.get("sdfg", "brak") -> brak
    # result = choose_type_calculation_function[type_calculation](first_number, second_number)
    _function = choose_type_calculation_function[type_calculation]
    result = _function(first_number, second_number)
    print(result)
    return result


if __name__ == "__main__":
    main = main3
    first_number = get_first_number()
    while True:
        first_number = main(first_number)

    # first_number = get_first_number()
    # second_number = get_second_number()
    # if type_of_calculation == 1:
    #     result = add_numbers(first_number, second_number)
    # elif type_of_calculation == 2:
    #     result = substraction_number(first_number, second_number)
    #
    # ...

    # print Wynik .....
