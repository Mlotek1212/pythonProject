def sort_key(item):
    return (-item[1], item[0])

def checkio(text: str) -> str:
    letter_count = {}
    text = text.replace(" ", "").lower()

    for letter in text:
        if letter in " !@#$%^&*()><?:{}+_|][';/.,~`:-0987654321":
            continue
        if not letter in letter_count.keys():
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    sorted_letters = sorted(letter_count.items(), key=sort_key)

    return sorted_letters[0][0]


print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")