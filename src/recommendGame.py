def generate_question(question, option1, option2):
    answer = input(f"{question}\n$ ")
    if option1 in answer:
        return True
    else:
        return False


def main():
    if generate_question("Do you like fighting games?", "yes", "no"):
        if generate_question("Do like RPGs or shooters?", "RPGs", "Shooters"):
            if generate_question("Do you like single player or multiplayer games?", "single", "multiplayer"):
                if generate_question("Do you want an open world or linear game?", "open world", "linear"):
                    game = "Zelda, Breath of the Wild"
                else:
                    game = "Final Fantasy VII"
            else:
                game = "Final Fantasy XIV"
        else:
            if generate_question("Do you like 1st or 3rd person shooters?", "1st", "3rd"):
                game = "Destiny 2"
            else:
                game = "Fortnite"
    else:
        if generate_question("Would you rather play a platformer or a simulator?", "platformer", "simulator"):
            if generate_question("Would you like the difficulty to be hard or easy?", "hard", "easy"):
                game = "Pogostuck 2"
            else:
                game = "Mario"
        else:
            if generate_question("Would you rather play a life simulator or a survival simulator?", "life", "survival"):
                game = "Animal Crossing"
            else:
                game = "Minecraft"
    print(f"I would recommend that you play {game}.")


if __name__ == '__main__':
    main()
