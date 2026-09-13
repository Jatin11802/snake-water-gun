import random 

computer = random.choice([-1,0,1])
user = input("Enter Your Choice [s , w , g] : ") 
Dict = { "s" : 1 , "w" : 0 , "g" : -1} 
reverseDict = {1 : "Snake" , 0 : "Water" , -1 : "Gun"}

if user in Dict: 
    you = Dict[user] 
    print(f"You Chose: {reverseDict[you]} \nComputer Chose: {reverseDict[computer]}") 

    if(you == 1 and computer == 1): 
        print("It's a Tie , computer and you both chose Snake. Try again!") 

    elif(you == 0 and computer == 0):
        print("It's a Tie , computer and you both chose Water. Try again!") 

    elif(you == -1 and computer == -1):
         print("It's a Tie , computer and you both chose Water. Try again!")

    elif(you == 1 and computer == 0):
         print("Congratulations You WON!!. Play again!")

    elif(you == 1 and computer == -1):
         print("Oh no, You LOST! Better Luck Next Time.")

    elif(you == 0 and computer == 1):
         print("Oh no, You LOST! Better Luck Next Time.")

    elif(you == 0 and computer == -1):
         print("Congratulations You WON!!. Play again!")

    elif(you == -1 and computer == 1):
         print("Congratulations You WON!!. Play again!")

    elif(you == -1 and computer == 0):
         print("Oh no, You LOST! Better Luck Next Time.")

else: print("Invlid Entry.")