# Pattern @345#
from state_machine import StateMachine


def state_zero(text: str):
    try:
        char, text = text[0], text[1:]
    except IndexError:
        return "error_state", text
    if char == "@":
        return "first_state", text
    return "start_state", text


def state_one(text: str):
    try:
        char, text = text[0], text[1:]
    except IndexError:
        return "error_state", text
    if char in [str(x) for x in range(10)]:
        return "second_state", text
    if char == "@":
        return "first_state", text
    return "start_state", text


def state_two(text: str):
    try:
        char, text = text[0], text[1:]
    except IndexError:
        return "error_state", text
    if char in [str(x) for x in range(10)]:
        return "second_state", text
    if char == "@":
        return "first_state", text
    if char == "#":
        return "third_state", text
    return "start_state", text


def state_three(text: str):
    try:
        char, text = text[0], text[1:]
    except IndexError:
        return "last_state", text

    if char == "@":
        return "first_state", text
    return "start_state", text


if __name__ == "__main__":
    m = StateMachine()
    m.add_state("start_state", state_zero)
    m.add_state("first_state", state_one)
    m.add_state("second_state", state_two)
    m.add_state("third_state", state_three)
    m.add_state("last_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("start_state")
    m.run("@234#")
    m.run("1@638#")
    m.run("@139#1")

