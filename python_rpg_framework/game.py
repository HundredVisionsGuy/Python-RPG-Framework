import character
import chapter_one

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
    exposite(chapter_one.backstory)
