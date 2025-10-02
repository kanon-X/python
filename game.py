'''
1 for snack
-1 for water
0 for gun
'''

computer = -1
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0 }
you = youDict[youstr]
if(computer == you):
    print("Match Tie")
else:
  if(computer == -1 and you ==1):
    print("You win")
  elif(computer == 1 and you == 0):
    print("you Lose")
  elif(computer == 1 and you == -1):
    print("You Lose")
  elif(computer == 1 and you == 0):
    print("You win")
  elif(computer == 0 and you == -1):
    print("You win")
  elif(computer == 0 and you == 1):
    print("You Lose")
  else:
    print("Match Tie")