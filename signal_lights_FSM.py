from random import randint

from state_machine import StateMachine


def state_red(timer_input, next_input=randint(0, 1)):
    if timer_input == 1:
        return "green", next_input
    if timer_input == 0:
        return "red", next_input


def state_green(timer_input, next_input=randint(0, 1)):
    if timer_input == 1:
        return "yellow", next_input
    if timer_input == 0:
        return "green", next_input


def state_yellow(timer_input, next_input=randint(0, 1)):
    if timer_input == 1:
        return "red", next_input
    if timer_input == 0:
        return "yellow", next_input


if __name__ == "__main__":
    m = StateMachine()
    m.add_state("red", state_red)
    m.add_state("green", state_green)
    m.add_state("yellow", state_yellow)
    m.add_state("last_state", None, end_state=1)
    m.add_state("error_state", None, end_state=1)
    m.set_start("red")

    while True:
        m.run(randint(0, 1))
