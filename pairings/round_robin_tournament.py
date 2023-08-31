import sys
import ast

# This code finds pairs by using a circle method
# for a round-robin tournament (mostly done by ChatGPT).
# Script takes list of names in a string cast as argument
# e.g.: python speeddating.py "['Sergio', 'Matthias', 'Andrew']"
# Uneven lists do get a 'Joker' added

def round_robin_tournament(names):
    """
    The round_robin_tournament function takes a list of names as input
    and returns a list of rounds, where each round consists of pairs of participants.
    The code iterates over the number of rounds, creating matches by
    pairing players from the front and back of the list. After each round,
    the players are rotated in the list to generate new pairings for the next round.
    """
    num_players = len(names)
    if num_players % 2 != 0:
        names.append("Joker")  # Add a Joker player if the number of participants is odd
        num_players += 1

    num_rounds = num_players - 1
    matches_per_round = num_players // 2

    rounds = []
    for round_num in range(num_rounds):
        round_matches = []
        for match_num in range(matches_per_round):
            player1 = names[match_num]
            player2 = names[num_players - 1 - match_num]
            round_matches.append((player1, player2))
        rounds.append(round_matches)

        # Rotate the players in the list
        names.insert(1, names.pop())

    return rounds

# Main part:
if __name__ == "__main__":
    participants = ast.literal_eval(sys.argv[1])
    tournament_rounds = round_robin_tournament(participants)

    for round_num, matches in enumerate(tournament_rounds, start=1):
        print(f"Round {round_num}:")
        for match in matches:
            print(f"{match[0]}, {match[1]}")
        print()
