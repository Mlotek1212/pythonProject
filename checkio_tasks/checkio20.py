def backward_string_by_word(text: str) -> str:
    if len(text) == 0:
        return text

    words = text.split(' ')
    reversed_words = []

    for word in words:
        reversed_word = word[::-1]
        reversed_words.append(reversed_word)
    result = ' '.join(reversed_words)
    return result



print("Example:")
print(backward_string_by_word("hello world"))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
