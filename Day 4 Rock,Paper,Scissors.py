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

#Write your code below this line 👇

import random
choice = int(input("what do you choose ?Type 0 for rock,1 for paper ,2 for scissors :"))

if choice==0:
  print(rock)
elif choice==1:
  print(paper)
elif choice==2:
  print(scissors)
else:
  print("invalid input")

computer=random.randint(0,2)
print(computer)

if computer==0:
  print(rock)
elif computer==1:
  print(paper)
elif computer==2:
  print(scissors)

if (choice==0 and computer==1)or(choice==1 and computer==2)or(choice==2 and computer==0):
  print("you lose")
else:
  print("you win :)")
  
