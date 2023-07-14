FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def conecting_numbers(number: int):
    result = []
    _number = str(number)
    if (special_number := int(_number[-2:])) < 20 and special_number >0:
        value = number_less_than_20(special_number)
        result.append(value)
        _number = _number[:-2] + "00"

    for i, char in enumerate(_number[::-1]):
        if i == 0:
            if char == '0':
                continue
            value = FIRST_TEN[int(char) - 1]
        elif i == 1:
            if char == '0':
                continue
            value = OTHER_TENS[int(char) - 2]
        else:
            if char == '0':
                continue
            value = f'{FIRST_TEN[int(char) - 1]} {HUNDRED}'
        result.append(value)
    return " ".join(result[::-1])


def number_less_than_20(num):
    index = num - 1
    if num == 0:
        return ""
    if num < 10:
        return FIRST_TEN[index]
    elif num < 20:
        return SECOND_TEN[num - 10]
    return ""


def checkio(num: int) -> str:
    if number_less_than_20(num):
        return number_less_than_20(num)
    return conecting_numbers(num)

# print('123456789'[0])
# print('123456789'[1:])
# print('123456789'[1:7])
# print('123456789'[1:7:3])
# print('123456789'[::-1])
# print(conecting_numbers(123))
# print("Example:")
# print(checkio(4))
#
# These "asserts" are used for self-checking
assert checkio(1) == "one"
assert checkio(2) == "two"
assert checkio(3) == "three"
assert checkio(4) == "four"
assert checkio(5) == "five"
assert checkio(6) == "six"
assert checkio(9) == "nine"
assert checkio(10) == "ten"
assert checkio(11) == "eleven"
assert checkio(12) == "twelve"
assert checkio(13) == "thirteen"
assert checkio(14) == "fourteen"
assert checkio(15) == "fifteen"
assert checkio(16) == "sixteen"
assert checkio(17) == "seventeen"
assert checkio(18) == "eighteen"
assert checkio(19) == "nineteen"
assert checkio(999) == "nine hundred ninety nine"
assert checkio(784) == "seven hundred eighty four"
assert checkio(777) == "seven hundred seventy seven"
assert checkio(88) == "eighty eight"
assert checkio(44) == "forty four"
assert checkio(20) == "twenty"
assert checkio(30) == "thirty"
assert checkio(40) == "forty"
assert checkio(50) == "fifty"
assert checkio(80) == "eighty"
assert checkio(90) == "ninety"
assert checkio(100) == "one hundred"
assert checkio(200) == "two hundred"
assert checkio(300) == "three hundred"
assert checkio(600) == "six hundred"
assert checkio(700) == "seven hundred"
assert checkio(900) == "nine hundred"
assert checkio(21) == "twenty one"
assert checkio(312) == "three hundred twelve"
assert checkio(302) == "three hundred two"
assert checkio(509) == "five hundred nine"
assert checkio(753) == "seven hundred fifty three"
assert checkio(940) == "nine hundred forty"
assert checkio(999) == "nine hundred ninety nine"
