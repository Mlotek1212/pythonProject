def amount_full_consumed_food(minute: int) -> int:    #ok
    if minute <= 1:
        return minute

    result = amount_bird(minute) + amount_full_consumed_food(minute - 1)
    return result


def amount_bird(minute):  #ok
    return sum(range(minute + 1))


def checkio(food: int) -> int:
    minute = 1
    if food == 1:   #ok
        return 1

    fed_birds_per_minute = []
    while True:
        food_birds: int = amount_full_consumed_food(minute)
        if food == food_birds:  #ok
            fed_birds_per_minute.append(amount_bird(minute))
            return max(fed_birds_per_minute)
        elif food < food_birds:
            used_food: int = food_birds - food
            max_food_for_minute = amount_bird(minute)
            fed_birds_per_minute.append(max_food_for_minute - used_food)
            return max(fed_birds_per_minute)
        elif food >= food_birds:
            fed_birds_per_minute.append(amount_bird(minute))
        minute += 1


# print(checkio(5))
assert checkio(27) == 10
assert checkio(18) == 8
# assert checkio(1) == 1
assert checkio(3) == 2
assert checkio(8) == 4
assert checkio(10) == 6
assert checkio(20) == 10
assert checkio(35) == 15
# assert amount_full_consumed_food(1) == 1
# assert amount_full_consumed_food(2) == 4
# assert amount_full_consumed_food(3) == 10
# assert amount_full_consumed_food(4) == 20
# assert amount_full_consumed_food(5) == 35


print("The mission is done! Click 'Check Solution' to earn rewards!")
#
# n + n
# 1 -> 1
# 2 -> 1 + 2 = 3
# 3 -> 3 + 3 = 6
# 4 -> 6 + 4 = 10
# (n - 1) + n
#
# jedzenie(miuta-1) + jedzenie(ilosc_g(minuta-1) + minuta)
# 1
# 1 + jedzenie(1 + 2)
