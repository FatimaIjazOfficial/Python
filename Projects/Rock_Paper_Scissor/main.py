# 21 scissors cutting paper,10 paper covering rock, and 02 rock crushing scissors
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
me = int(input("What do you choose : (0)Rock (1)Paper (2)Scissor ? "))
computer = random.randint(0, 2)
if me == 0 or me == 1 or me == 2:
    if me == 0:
        print(f"Me : Rock\n {rock}")
    if me == 1:
        print(f"Me : paper\n {paper}")
    if me == 2:
        print(f"Me : scissor\n {scissors}")
    if computer == 0:
        print(f"Computer : Rock\n {rock}")
    if computer == 1:
        print(f"Computer : paper\n {paper}")
    if computer == 2:
        print(f"Computer : scissor\n {scissors}")
    if me == 0 and computer == 0:
        print("Tie")
    elif me == 0 and computer == 1:
        print("Computer Win")
    elif me == 0 and computer == 2:
        print("You Win")
    elif me == 1 and computer == 0:
        print("You Win")
    elif me == 1 and computer == 1:
        print("Tie")
    elif me == 1 and computer == 2:
        print("Computer Win")
    elif me == 2 and computer == 0:
        print("Computer Win")
    elif me == 2 and computer == 1:
        print("You Win")
    elif me == 2 and computer == 2:
        print("Tie")
else:
    print("Again Enter Number B/W 0-2")
