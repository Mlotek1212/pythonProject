def validate_number(number: int|float, which_number: int) -> bool:
    ...


def validate(first: int|float, second: int|float) -> bool:
    ...


def add_numbers(first, second):
    if not validate(first, second):
        return

    if not isinstance(first, (int, float)):
        print("Podałeś błędną pierwszą wartoś")
        return
    if not isinstance(second, (int, float)):
        print("Podałeś błędną drugą wartoś")
        return
    return first + second


def subtraction_numbers(first, second):
    if not validate(first, second):
        return

    if not isinstance(first, (int, float)):
        print("Podałeś błędną pierwszą wartoś")
        return
    if not isinstance(second, (int, float)):
        print("Podałeś błędną drugą wartoś")
        return
    return first - second

def multiplication_numbers(first, second):
        if not validate(first, second):
            return

        if not isinstance(first, (int, float)):
            print("Podałeś błędną pierwszą wartoś")
            return
        if not isinstance(second, (int, float)):
            print("Podałeś błędną drugą wartoś")
            return
        return first * second


def  sharing_numbers(first, second):
    if not validate(first, second):
        return

    if not isinstance(first, (int, float)):
        print("Podałeś błędną pierwszą wartoś")
        return
    if not isinstance(second, (int, float)):
        print("Podałeś błędną drugą wartoś")
        return
    return first / second

def compounding_numbers(first, second):
        if not validate(first, second):
            return

        if not isinstance(first, (int, float)):
            print("Podałeś błędną pierwszą wartoś")
            return
        if not isinstance(second, (int, float)):
            print("Podałeś błędną drugą wartoś")
            return
        return first ** second

# pierwiastkowanie



def validate_error(type_calculation):
    ...


def get_type_of_calculation():
    type_calculation = int(input("""wybierz rodzaj działania :
     1.dodawanie
     2.odejmowanie
     3.mnożenie
     4.dzielenie
     5.potęgowanie"""))
   if type_calculation >=5 and <=1:
       print()


# validate_error -> int -> musi się zawierać w wartościach które są dostępne
    # if validate_error:
    #     "podałeś błędną wartość podaj jeszcze raz"
    #     print(validate_error)
    #     return get_type_of_calculation()



def main():
    ...
    # print_posible_events()
    # type_of_calculation = get_type_of_calculation()
    # first_number = get_first_number()
    # second_number = get_second_number()
    # if type_of_calculation == 1:
    #     result = add_numbers(first_number, second_number)
    # elif type_of_calculation == 2:
    #     result = substraction_number(first_number, second_number)
    #
    # ...

    # print Wynik .....


if __name__ == '__main__':
    i = 0
    while i < 5:
        i = i + 1
        main()
