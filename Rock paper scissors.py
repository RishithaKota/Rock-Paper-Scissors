import random
p=int(input(print("How many times do you want to play this game?")))
you=0
computer=0
for i in range (p):
 print("Rock = 0, Paper = 1, Scissor = 2")

 ch=int(input(print("Enter your choice: ")))
 if (ch>=3):
     print("Invalid choice")
 set= {1,2,3}
 element_index = random.randrange(0, len(set))
 com = list(set)[element_index]

 if (ch==com):
     print("Draw")
 elif (ch==0 and com==2):
     print("You win!")
     you+=1
 elif (ch==0 and  com==1):
     print("Computer wins!")
     computer+=1
 elif(ch==1 and com==2):
     print("Computer wins!")
     computer+=1
 elif(ch==1 and com==0):
     print("You win!")
     you+=1
 elif(ch==2 and com==0):
     print("Computer wins!")
     computer+=1
 elif(ch==2 and com==1):
     print("You win!")
     you+=1

 print("Your score: ", you)
 print("Computer's score: ",computer)
 



