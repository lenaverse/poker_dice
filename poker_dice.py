"""
POKER DICE

User vs computer will compete to get the best possible dice hand:

FIVE OF A KIND (4-4-4-4-4)  -> 50 points
FOUR OF A KIND (3-3-3-3-6)  -> 30 points
FULL HOUSE (5-5-5-2-2)      -> 20 points
THREE OF A KIND (1-1-1-3-4) -> 15 points
TWO PAIRS (2-2-5-5-4)       -> 5 points
ONE PAIR (4-4-1-2-6)        -> 2 points
HIGHEST RANKING DIE         -> 1 point

Each player gets three rolls. They can choose to reroll any number of dice.
They can also choose to only roll once or twice if they're happy
with the dice hand.

"""

"""
USER TURN
- Roll dice and store in [hand]
- Display score
- If rerolls < 2:
    - Ask if they want to reroll
    - If yes, ask which dice
    - If no, end turn and display final score. Move on to computer turn

COMPUTER TURN
- Roll dice and store in [hand]
- Display score
- Computer should always aim to get a higher score.
    - Keep whatever is best from hand
        - E.g. keep any repeated dice
        - If no repeats, keep highest scoring dice (maybe 50% chance
        to reroll all?)
"""

"""
DICE:
- 6 = ACE
- 5 = KING
- 4 = QUEEN
- 3 = JACK
- 2 = 10
- 1 = 9
"""


from random import choice
user_hand = []

ai_hand = []


def roll_dice(dice_num: int = 5) -> list[int]:
    roll = []

    for i in range(dice_num):
        roll.append(choice([1, 2, 3, 4, 5, 6]))

    return roll


def is_player_turn() -> bool:

    print("Welcome to Poker dice! This is your starting hand: ")
    user_hand = roll_dice()
    print(user_hand)

    num_rolls = 1
    while True:
        if num_rolls == 3:
            print(
                f"You can't reroll anymore! Your score is {calculate_points(user_hand)}.")
            return False

        player_choice = input("What would you like to do? (Reroll/End turn): ")
        if player_choice.lower() == "end turn":
            print(f"Your score is {calculate_points(user_hand)}.")
            return False
        elif player_choice.lower() == "reroll":
            player_choice_reroll = input(
                "Which dice would you like to reroll? (Enter positions "
                "1 to 5 separated by spaces or All to reroll whole hand): ")
            if player_choice_reroll.lower() == "all":
                user_hand = roll_dice()
                print(f"This is your hand: {user_hand}")
                num_rolls += 1
            else:
                reroll_positions = player_choice_reroll.split()
                for position in reroll_positions:
                    user_hand[(int(position))-1] = 0
                user_hand = [roll for roll in user_hand if roll != 0]
                user_hand.extend(roll_dice(5 - len(user_hand)))
                print(f"This is your hand: {user_hand}")
                num_rolls += 1
        else:
            print("Please enter a valid option.")


def ai_turn() -> bool:
    print("COMPUTER TURN. This is their starting hand: ")
    ai_hand = roll_dice()
    print(ai_hand)


def calculate_points(dice_hand: list[int]) -> int:
    score_chart = {
        "Five of a kind": 50,
        "Four of a kind": 30,
        "Full house": 20,
        "Three of a kind": 15,
        "Two pairs": 5,
        "One pair": 2,
        "Highest ranking die": 1
    }

    if len(set(dice_hand)) == 1:
        return score_chart["Five of a kind"]

    if any(dice_hand.count(roll) == 4 for roll in dice_hand):
        return score_chart["Four of a kind"]

    if any(dice_hand.count(roll) == 3 for roll in dice_hand):
        if len(set(dice_hand)) == 2:
            return score_chart["Full house"]
        return score_chart["Three of a kind"]

    if any(dice_hand.count(roll) == 2 for roll in dice_hand):
        if len(set(dice_hand)) == 3:
            return score_chart["Two pairs"]
        return score_chart["One pair"]
    return score_chart["Highest ranking die"]


def play() -> None:

    is_player_turn()


if __name__ == "__main__":
    play()
