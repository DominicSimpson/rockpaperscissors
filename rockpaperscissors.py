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


choices = [rock, paper, scissors]

number_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))

computer_input = random.randint(0, 2)

if number_input >= 3 or number_input < 0:
    print("Please input only numbers from 0 to 2")
else:
    print("You chose:")
    print(choices[number_input])

    print("Computer chose:")
    print(choices[computer_input])

if computer_input == number_input:
    print("It's a Draw!")
elif (computer_input == 0 and number_input == 2) or \
    (computer_input == 1 and number_input == 0) or \
        (computer_input == 2 and number_input == 1):
    print("The computer wins! You lose")
elif (number_input == 0 and computer_input == 2) or \
    (number_input == 1 and computer_input == 0) or \
        (number_input == 2 and computer_input == 1):
    print("You win! Well done")
