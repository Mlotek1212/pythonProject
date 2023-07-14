def middle(text: str) -> str:
    if len(text) == 1:
        return text

    elif len(text) % 2 == 0:
        split = round(len(text) / 2)

        return text[split - 1: split + 1]

    else:
        split = round((len(text) / 2) + 0.01)

        return text[split - 1]
print(middle("toudi"))
