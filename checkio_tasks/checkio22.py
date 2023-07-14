def forward(position_x, position_y):
    return position_x, position_y + 1


key_map = {
    'f': forward,
    # 'f': lambda position_x, position_y: (position_x, position_y + 1),
    'b': lambda position_x, position_y: (position_x, position_y - 1),
    'r': lambda position_x, position_y: (position_x + 1, position_y),
    'l': lambda position_x, position_y: (position_x - 1, position_y),
}


def follow(instructions: str) -> tuple[int, int] | list[int]:
    coordinates = [0, 0]
    for step in instructions:
        if step not in key_map.keys():
            continue
        coordinates = key_map[step](*coordinates)
    return coordinates


print("Example:")
print(list(follow("fflff")))

# These "asserts" are used for self-checking
assert list(follow("fflff")) == [-1, 4]
assert list(follow("ffrff")) == [1, 4]
assert list(follow("fblr")) == [0, 0]

print("The mission is done! Click 'Check Solution' to earn rewards!")