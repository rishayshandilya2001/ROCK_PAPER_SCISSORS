import random
choices=["rock","paper","scissors"]
print("___________ROCK_PAPER_SCISSORS_GAME______________\n")
ch=int(input("enter 0 for rock , 1 for paper , 2 for scissors\n"))
print("\n")
print(f"user choose {choices[ch]}")
if(choices[ch]=="rock"):
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif(choices[ch]=="paper"):
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif(choices[ch]=="scissors"):
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    
computer=random.choice(choices)
user=choices[ch]
print(f"computer choose {computer}")
if(computer=="rock"):
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif(computer=="paper"):
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif(computer=="scissors"):
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if(user=="rock" and  computer=="paper"):
    print("you loose")
elif(user=="rock" and  computer=="scissors"):
    print("you win")
elif(user=="rock" and  computer=="rock"):
    print("match draw")
elif(user=="paper" and  computer=="rock"):
    print("you win")
elif(user=="paper" and  computer=="paper"):
    print("match draw")
elif(user=="paper" and  computer=="scissors"):
    print("you win")
elif(user=="scissors" and  computer=="rock"):
    print("you loose")
elif(user=="scissors" and  computer=="scissors"):
    print("match draw")
elif(user=="scissors" and  computer=="paper"):
    print("you won")


