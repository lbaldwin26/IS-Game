from model import queue
from multithreading import Thread
import sys


def _match_finder(queue):
    while True:
        q_len = len(queue)
        if q_len >= 2:
            player_one = queue.popleft()
            player_two = queue.popleft()

            player_one.send_packet()
            player_two.send_packet()

        sys.sleep(5)


match_finder_process = Thread(
    target=_match_finder,
    args=[queue],  # ISSUE 1: Is this a reference or a copy? Will it react to changes
)
