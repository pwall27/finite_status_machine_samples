from exceptions import InitializationError


class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.start_state = None
        self.end_states = []

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.end_states.append(name)

    def set_start(self, name):
        self.start_state = name.upper()

    def get_handler(self, state=None):
        state = self.start_state if not state else state.upper()
        handler = self.handlers.get(state)
        if not handler:
            raise InitializationError("must call .set_start() before .run()")
        return handler

    def run(self, cargo):
        handler = self.get_handler()
        if not self.end_states:
            raise InitializationError("at least one state must be an end_state")

        while True:
            (new_state, cargo) = handler(cargo)
            if new_state.upper() in self.end_states:
                return f"reached {new_state} which is an end state"
            else:
                handler = self.get_handler(new_state)
