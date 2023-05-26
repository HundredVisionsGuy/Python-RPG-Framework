import character
import chapter_one
import utilities

main_menu = """
MAIN MENU:
1.  Start New Game
2.  Continue Game
3.  Save Game
4.  Quit
"""

def main():
    # Show main menu until the user quits
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(main_menu,
                                           ("1", "2", "3", "4"))
        if choice == "1":
            exposite(chapter_one.backstory)
        if choice == "4":
            print("\nThanks for playing")

def exposite(text: tuple):
    for paragraph in text:
        # if not the last paragraph, add a ...
        if paragraph != text[-1]:
            description = paragraph
            description += "\n\033[3m\033[95m\033[40mPress enter to continue...\033[0m"
            input(description)
        else:
            input("\n" + paragraph)

if __name__ == "__main__":
    main()
