import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input("Welcome to rock, paper, scissors. Please type 0 for rock, 1 for paper and 2 for scissors: "))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == computer_choice:
    print("Its a tie!")
elif user_choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins!")
else:
    print("Please write a valid number and try again!")
