from random import randint

choice = ["Rock", "Paper", "Scissor"]
computer = choice[randint(0, 2)]
player = True

while player:
    check = input('Do you want to play?(Y/N) ').title()
    if check == "Y":
        player = input('Enter "Rock" "Paper" or "Scissor": ').title()
        print(f"You picked {player} and Computer picked {computer}")
        if player == computer:
            print("Tie!!")

        elif player == "Rock" and computer == "Paper" or player == "Paper" and computer == "Scissor" or player == "Scissor" and computer == "Rock":
            print("You lost!!")

        elif player == "Rock" and computer == "Scissor" or player == "Paper" and computer == "Rock" or player == "Scissor" and computer == "Paper":
            print("You win!!")

        else:
            print("Please enter valid input!!")

        player = True
        computer = choice[randint(0, 2)]

    else:
        exit()
