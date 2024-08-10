from random import randint

choice = ["Rock", "Paper", "Scissor"]
computer = choice[randint(0, 2)]
player = False

while not player:
    check = input('Do you want to play?(Y/N) ').title()
    if check == "Y":
        player = input('Enter "Rock" "Paper" or "Scissor": ').title()
        if player == computer:
            print(f"You picked {player} and Computer picked {computer}")
            print("Tie!!")

        elif player == "Rock":
            if computer == "Paper":
                print(f"You picked {player} and Computer picked {computer}")
                print("You lost!!")
            elif computer == "Scissor":
                print(f"You picked {player} and Computer picked {computer}")
                print("You Win!!")

        elif player == "Paper":
            if computer == "Rock":
                print(f"You picked {player} and Computer picked {computer}")
                print("You win!!")
            elif computer == "Scissor":
                print(f"You picked {player} and Computer picked {computer}")
                print("You lost!!")

        elif player == "Scissor":
            if computer == "Paper":
                print(f"You picked {player} and Computer picked {computer}")
                print("You win!!")
            elif computer == "Rock":
                print(f"You picked {player} and Computer picked {computer}")
                print("You lost!!")

        else:
            print("Please enter valid input!!")

        player = False
        computer = choice[randint(0, 2)]

    else:
        exit()
