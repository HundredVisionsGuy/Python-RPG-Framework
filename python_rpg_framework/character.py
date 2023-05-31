""" character.py
The base class for the player and any NPCs in the game. Will have attributes
and behavior common to all characters
"""
import dm


class Character:
    """Any playing and non-playing characters share these traits

    Attributes:
        name: a string
        class_name: string name of character class
        strength: int physical power and carrying capacity
        dexterity: int agility, balance, coordination
        constitution: int endurance, stamina, health
        intelligence: int reasoning, knowledge, memory
        ...and so on (you choose which of these you want)"""

    def __init__(self, name: str, class_name="") -> None:
        self.name = name
        self.class_name = class_name

        # initialize all remaining stats (we'll create a function to set them)
        self.strength = dm.roll_stats()
        self.dexterity = dm.roll_stats()
        self.constitution = dm.roll_stats()
        self.intelligence = dm.roll_stats()
        self.attack_modifier = dm.get_modifier(self.strength)

    def get_stats(self) -> str:
        """ return a formatted string of stats """
        stats = f"Name: {self.name}\nClass: {self.class_name}\n"
        stats += f"Strength: {self.strength}\nDexterity: {self.dexterity}"
        stats += f"\nConstitution: {self.constitution}"
        stats += f"\nIntelligence: {self.intelligence}"
        stats += f"\nAttack Modifier: {self.attack_modifier}"
        return stats

# global scope
if __name__ == "__main__":
    player = Character("Chris", "Half-orc")
    print(player.get_stats())
