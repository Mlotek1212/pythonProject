def non_empty_lines_old(text: str) -> int:
    if len(text) == 0:
        return 0

    text_splited_by_line = text.split("\n")
    emply_line = 0

    for line in text_splited_by_line:

        if len(line) == 0 or line.isspace():
            emply_line += 1

    return len(text_splited_by_line) - emply_line


def non_empty_lines(text: str) -> int:
    return sum(
        [1 for line in text.split("\n")
         if len(line) > 0 and not line.isspace()
         ]
    )



print("Example:")
print(non_empty_lines("one simple line\n"))

# These "asserts" are used for self-checking
assert non_empty_lines("one simple line\n") == 1
assert non_empty_lines("") == 0
assert non_empty_lines("\nonly one line\n            ") == 1
assert (
    non_empty_lines(
        "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
    )
    == 3
)

print("The mission is done! Click 'Check Solution' to earn rewards!")