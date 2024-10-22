import time
import random

from debug import logger

from threading import Thread
from model import queue, players, States
from packets.QueueMatch import QueueMatch


def _match_finder(queue):
    while True:
        q_len = len(queue)
        if q_len >= 2:
            player_one = queue.popleft()
            player_two = queue.popleft()

            if not player_one.isOk:
                logger.debug("head of the queue left before finding a match")
                queue.appendleft(player_two)
                logger.debug(queue)
            else:
                gets_starting_turn = bool(random.randint(0, 1))

                player_one.send_packet(
                    QueueMatch(
                        player_two.UUID,
                        gets_starting_turn,
                    )
                )

                players[player_one.UUID]["state"] = States.IN_GAME
                players[player_one.UUID]["opponent"] = player_two.UUID

                player_two.send_packet(
                    QueueMatch(
                        player_one.UUID,
                        not gets_starting_turn,
                    )
                )

                players[player_two.UUID]["state"] = States.IN_GAME
                players[player_two.UUID]["opponent"] = player_one.UUID
        time.sleep(2)


match_finder_thread = Thread(
    target=_match_finder,
    args=[queue],
)

# Exit the thread when the main thread exits
match_finder_thread.daemon = True
