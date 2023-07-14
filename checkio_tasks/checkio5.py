def from_camel_case(name: str) -> str:
    resoult = ""
    ww = name[0]
    if ww in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        ww = ww.lower()
        resoult += ww
    for char in name:


        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            char = '_' + char.lower()
        resoult += char

    return resoult

print(from_camel_case("MyCar"))
