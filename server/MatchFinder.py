import time
import random


from threading import Thread
from model import queue, players, States
from packets.QueueMatch import QueueMatch

def make_match(player_one, player_two):
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

# Completely hacky way of doing things
def _match_finder(queue):
    while True:
        q_len = len(queue)
        if q_len >= 2:
            disconnected_clients_exist = False
            player_one = queue.popleft()
            player_two = queue.popleft()

            if not player_one.isOk:
                disconnected_clients_exist = True
                queue.appendleft(player_two)

            if not player_two.isOk:
                disconnected_clients_exist = True
                queue.appendleft(player_one)
            

            if not disconnected_clients_exist:
                make_match(player_one, player_two)

        time.sleep(2)


match_finder_thread = Thread(
    target=_match_finder,
    args=[queue],
)

match_finder_thread.daemon = True
