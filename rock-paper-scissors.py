import random
while True:
    print("Select rock, paper, or scissors below")
    print("rock \npaper \nscissors")
    choice = input()
    if(choice == " rock"):
        print(" Rock")
    elif(choice == " paper"):
        print(" paper")
    else:
        print(" scissors")
        possible_actions = ["Rock","Paper","Scissors"]
        computer_action = random.choice (possible_actions)
        print(f"\nYou Chose {choice}, computer chose {computer_action}\n")
    if computer_action == choice:
        print("tie")
    elif choice == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("You lose.")
    elif choice == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("You lose.")
    elif choice == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("You lose.")

    play_again = input("Play again? (y/n):")
    if play_again.lower() != "y":
        break
