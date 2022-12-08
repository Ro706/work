'''
Anshul and Ashish want to play a game where each of them enter a number alternatively.
The game continues for 11 rounds, a Anshul scores a point if the sum of the two numbers is a
prime number and Ashish scores a point of the sum is multiple of 4. The person with highest
point wins the game at the end. Write a program to implement it in C/python.
'''
def prime(n):
  list_1=[]
  a = n
  for i in range(n,n):
    for j in range(2,i):
      if i%j==0:
        break
    else:
      list_1.append(i) 
  if len(list_1) > 2:
    return ("you lose")
  else: 
    return ("you win")
    
            

scorea = 0
scoreb = 0 
num = 0
round = 0
while round != 23:
  turn= ["anshul","ashish"]
  if turn[num] == 'anshul' :
      n = int(input("anshul enter number:"))
      x = prime(n)
      num += 1 
      if x == "you win":
          scorea +=1
          print("you win")
      else:
          scorea +=0  
          print("sorry you lose")   
      round += 1

  else:
      n = int(input("ashish enter number:"))   
      x = prime(n)
      num -= 1
      if x == "you win":
          scoreb +=1
          scorea +=1
          print("you win")
      else:
          scoreb +=0  
          print("sorry you lose")   
      round += 1
if scorea == scoreb:  
   print("tie")   
elif scorea > scoreb:
   print('anshul you win the match')
else:
  print('ashish you win the match')

'''
A train is scheduled to travel between two cities A and B. There are ‘n’ halting stations for
the journey such that the train halts at specific stations based on the distance between the
stations. The first halt is at a distance of 5km from city A and second halt is at 8km from first
halt. The remaining halts are at a distance of the sum of the distances of the previous two
halts. Write a program to print the distance of each halt one after the another up to ‘n’ halts to
reach city B. Write a program to implement this in C/python.
'''
def fibb(n):
  a,b = 5,8
  while a < n:
    print(a,end =" ")
    a, b = b,(a+b)
n = int(input("enter number halting stations:"))
fibb(n)

'''
A roller and costar ride of diameter 10-meter runs for some number of rounds based on the
number of people onboard in the ride (Assume 50 kg weight of each rider). What should be
the maximum velocity of rotation at an angle of 12.13 degree, if a centrifugal force acting on
each object is 47 N such that the riders are safe.
'''
import math
n = int(input("enter no of person:"))
m = 50 * n
g = 10*n
v =( (5*g*math.tan(12.13))**(1/2))
print(v.real)

'''
Dhairya wants to participate in a 400 m racing competition, in order to be eligible for it he
needs to finish the trial race in 58 sec. Dhairya runs a lap on a track of 100 m and records its
time and continue to run for total 4 laps. At last he computes total time required for 400 m.
Write a program to let Dhairya know by how much seconds he needs to improve his speed in
order to be eligible for the final competition. Write a program to implement it in C/python.
'''
n = int(input("enter the time coverd in 400m(in second):"))
if n<= 58 :
  print("dhairya's speed is already up to be eigible for the 400 m racing comp4tion")
else:
  print(f'dhairya need to improve his speed by {n - 58} sec')

'''
Rohit creates a game such that, when a player enters his date of birth, the program computes
single digit sum of it and displays a message based on the sum as follows: if sum is
1: You are Intelligent, 2: You are Handsome, 3: You are Cool, 4: You are Dangerous, 5:
You are Gorgeous, 6: You are Smart, 7: You are Funny, 8: You are Genius, 9: You are
Crazy
Note: if dob is 14 then sum is 5 (1 + 4 = 5) but if dob is 29 sum is 2 (2 + 9 = 11  1 + 1 = 2)
'''
dob = str(input("enter your date of birth (01-31):"))
dob = int(dob[0])+int(dob[1])
date = {1:"You are Intelligent",2:"You are Handsome",3:"You are Cool",4:" You are Dangerous",5:"You are Gorgeous",6:"You are Smart",7:"You are Funny",8:" You are Genius",9:"You are Crazy"}
mylist=date.items()
for x in mylist:
    n = dob
    if x[0] == n:
        print(x[1])
    else:
        continue
