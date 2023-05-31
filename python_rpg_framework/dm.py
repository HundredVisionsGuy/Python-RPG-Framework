"""dm.py: The Dungeon Master (DM) for our program"""

import random


def roll_stats() -> int:
    """get stats for a character's attributes
    
    Standard Algorithm in DnD: FTW (For The Win)
        SET dice_rolls to empty list
        REPEAT 4 times
            SET random number between 1 and 6
            APPEND number to dice_rolls
        SORT dice_rolls
        POP lowest number

    My Simplified Algorith:
    simulate that behavior from above: return a 
    random number between 6 and 18"""
    stats = random.randint(6, 18)
    return stats


def get_modifier(stat: int) -> int:
    """Returns a modifier based on the stat value

    For the Win: use the following table:
    https://www.modularrealms.com/en-us/blogs/news/how-do-dnd-stats-work
    """
    modifier = 0
    # TODO (FTW: For the Win)
    # use the table from 
    return modifier


if __name__ == "__main__":
    for i in range(5):
        print(roll_stats())