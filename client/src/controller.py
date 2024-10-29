states = {
    "DISCONNECTED": None,
    "IDLE": None,
    "MATCH_MAKING": None,
    "IN_GAME": None,
}

current_state = states["IDLE"]

class State:
    def __init__(self, available_states):
        self.available_states = available_states
