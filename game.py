# rock, paper and scissors game
import random
def main(): 
    is_running = True
    while is_running:
        print("rock, paper and scissors game".title())
        print("*" * 70)
        options = [ 'rock', 'paper', 'scissors']
        computer = random.choice(options)
        player = input("rock , paper , scissors (Q) to quit\n")
        if player == "q".lower():
            is_running = False
            print("*" * 70)
            print("thank you for playing with us".upper())
            print("*" * 70)
        else:
            if computer == player:
                print("it's a tie")

            elif computer == "rock" and player == "paper":
                print("paper covers rock. \nplayer wins..".title())
            
            elif computer == "paper" and player == "rock":
                print("paper covers rock. \ncomputer wins".title())
                
                
            elif computer == "paper" and player == "scissors":
                print("scissors cuts paper. \nplayer wins.".title())
                
                
            elif computer == "scissors" and player == "paper":
                print("scissors cuts paper. \ncomputer wins.".title())
                
                
            elif computer == "scissors" and player == "rock":
                print("rock breaks scissors. \nplayer wins.".title())
                
                
            elif computer == "rock" and player == "scissors":
                print("rock breaks scissors. \ncomputer wins.".title())
            
                
            else:
                print("Invalid choice.".title())

if __name__ == "__main__" :
    main()
