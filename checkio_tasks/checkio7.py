def to_camel_case_old(name: str) -> str:
    result = ""
    flag_next = False

    for i, char in enumerate(name):
        if i == 0:
            char = char.upper()
        if i == 0 and char == char.upper():
            result += char.upper()
            continue



        if char == '_' and len(name) <= i+1:
            name[i+1] = name[i+1].upper()
            flag_next = True
        else:
            if flag_next:
                char = char.upper()
                flag_next = False
            else:
                char = char.lower()
            result += char

    return result


def to_camel_case(name: str) -> str:
    # breakpoint()
    # title_word = [word.title() for word in name.split("_")]
    # result = ""
    # for item in title_word:
    #     result += item
    # "".join(title_word)

    return "".join([word.title() for word in name.split("_")])

print(to_camel_case("my_function_name"))