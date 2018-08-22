

def stop_state(timer_input: int, trucks_waiting: bool):
    state = "stop" if timer_input == 0 else "go"
    pollution = trucks_waiting and state == "stop"
    return state, pollution


def go_state(timer_input: int, trucks_waiting: bool):
    state = "go" if timer_input == 0 else "stop"
    pollution = False
    return state, pollution


def doing_pollution(state: str, trucks_waiting: bool, transaction: int):
    switch = {
        "go": go_state,
        "stop": stop_state
    }
    func = switch.get(state, lambda: None)
    return func(transaction, trucks_waiting)
