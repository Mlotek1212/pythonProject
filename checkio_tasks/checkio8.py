def cut_sentence(line: str, length: int) -> str:
    result = ""
    used_char = 0
    for i, word in enumerate(line.split(" ")):
        used_char += (len(word) if i == 0 else len(word) + 1)
        if used_char > length:
            result += "..."
            return result
        else:
            result += f"{' ' if i > 0 else '' }{word}"
    return result

# name = "Bartek"
# a_in_name = "+" if "a" in name else "-"
# print("Example:")
# print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")