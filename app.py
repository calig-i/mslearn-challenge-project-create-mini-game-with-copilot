import random

# write 'hello world' to the browser
# print('hello world')

# game rules:

# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.















# # Create two players, one for the computer and one for the user.

# class Player:
#     def __init__(self, name):
#         self.name = name

#     def choose_option(self):
#         option = input("Enter your choice (rock, paper, scissors): ")
#         if option.lower() not in ["rock", "paper", "scissors"]:
#             print("Invalid option. Please choose rock, paper, or scissors.")
#             return self.choose_option()
#         return option.lower()

# computer = Player("Computer")
# user = Player("User")

# def play_round(user_choice):
#     computer_choice = random.choice(["rock", "paper", "scissors"])
    
#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif user_choice == "rock" and computer_choice == "scissors":
#         print("You win!")
#     elif user_choice == "scissors" and computer_choice == "paper":
#         print("You win!")
#     elif user_choice == "paper" and computer_choice == "rock":
#         print("You win!")
#     else:  
#         print("Computer wins!")

# def play_game():
#     while True:
#         print("Choose an option:")
#         print("rock")
#         print("paper")
#         print("scissors")
#         print("quit")
        
#         choice = input("Enter your choice: ")
        
#         if choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors":
#             if choice == "quit":
#                 print("Thanks for playing!")
#                 break
#             play_round(choice.lower())
#         else:
#             print("Invalid choice. Please try again.")

# play_game()

