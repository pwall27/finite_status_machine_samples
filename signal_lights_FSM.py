from random import randint


def state_red(timer_input):
    if timer_input == 1:
        return "green"
    if timer_input == 0:
        return "red"


def state_green(timer_input):
    if timer_input == 1:
        return "yellow"
    if timer_input == 0:
        return "green"


def state_yellow(timer_input):
    if timer_input == 1:
        return "red"
    if timer_input == 0:
        return "yellow"


def run_fsm(state: str, transaction: int):
    switch = {
        "red": state_red,
        "green": state_green,
        "yellow": state_yellow
    }
    func = switch.get(state, lambda: None)
    return func(transaction)


# if __name__ == "__main__":
#     st = "red"
#     while True:
#         st = run_fsm(st, randint(0, 1))
#         print(f"Transaction at: {st}")
