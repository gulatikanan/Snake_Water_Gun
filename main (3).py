# 0- snake, 1-water,2=gun
import random
user = int(input("choose 0 for snake, 1 for water, 2 for gun:\n"))
comp = random.randint(0,2)
def check(user,comp):
  if comp==user:
   return 0 #draw 
  if (comp== 0 and user == 1):
    return -1  #user loose
  if (comp == 1 and user==2):
    return -1 
  if(comp==2 and user==0):
    return -1
  return 1

score = check(user,comp)

print ("You:",user)
print("Computer",comp)


if(score==0):
  print("It's a draw")
elif (score== 1):
  print("you won")
else:
 print("you lose")
  
  
 