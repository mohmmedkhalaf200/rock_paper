import random

print ("star the game")

user = input("choose your move (R , P , S )")


#SOLUTION_1
# def my_list() :
#    return (random.choice(["P" , "R" , "S"]))
# PC = my_list()

#SOLUTION_2
# my_list = ["P" , "R" , "S"]

# PC = (random.choice(my_list))

#SOLUTION_3
PC = random.choice(["P" , "R" , "S"])

print("User played: " + user)
print("PC played: " + PC)

if user == PC :
   print ("it's a tie")
elif user == "P" and PC == "R" :
   print("User won")
elif user == "R" and PC == "S" :
   print("User won")  
elif user == "S" and PC == "P" :
   print("User winn") 
else :
   print ("You losee!")   

print("Game Over")   
