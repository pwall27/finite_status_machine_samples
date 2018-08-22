# Pattern @345#


def state_zero(char: str):
    if char == "@":
        return 1
    return 0


def state_one(char: str):
    if char in [str(x) for x in range(10)]:
        return 2
    return 1


def state_two(char: str):
    if char in [str(x) for x in range(10)]:
        return 2

    if char == "@":
        return 1

    if char == "#":
        return 3

    return 0


def state_three(char: str):
    if char == "@":
        return 1
    return 0


def match(string: str):
    state = 0
    states = {
        0: state_zero,
        1: state_one,
        2: state_two,
        3: state_three
    }
    for char in string:
        state = states[state](char)

    return state == 3

