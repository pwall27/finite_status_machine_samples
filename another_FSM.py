from random import randint


def state_i(entry: str or int):
    if entry == 0:
        return "i"
    if entry == 1:
        return 0


def state_0(entry: str or int):
    if entry == 0:
        return 1
    if entry == 1:
        return 2


def state_1(entry: str or int):
    if entry == 0:
        return 0
    if entry == 1:
        return 2


def state_2(entry: str or int):
    if entry == 1:
        return 0
    if entry == 0:
        return 1


def run_fsm():
    state = "i"
    switch = {
        "i": state_i,
        0: state_0,
        1: state_1,
        2: state_2
    }

    while True:
        func = switch.get(state, lambda: None)
        state = func(randint(0, 1))
        print(f"Transaction at: {state}")


run_fsm()