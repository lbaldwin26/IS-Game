from collections import deque
from enum import Enum

queue = deque()

players = {}


class States(Enum):
    DISCONNECTED = 1
    IDLE = 2
    MATCH_MAKING = 3
    IN_GAME = 4
