import random
flag=0
while True:
    user=input("Enter your choice (rock,paper,scissor) : ")
    
    print("User's choice is : ",user)
    options=['rock','paper','scissor']
    computer=random.choice(options)
    print("Computer's choice : ",computer)
    if(user!='rock' and user!='paper' and user!='scissor'):
        print("INVALID CHOICE")

    if(user==computer):
        
        print("IT'S A TIE!!!")
        

    elif(user=='rock' and computer=='scissor'
     or user=='paper' and computer=='rock'
     or user=='scissor' and computer=='paper'):
        
        print("CONGRATULATIONS YOU WON!!!")
        
        flag=flag+1

    else:
        print("OOPS YOU LOST!!!")
        
    ch=input("Do you want to play again -->")
    if ch=='n':
        print("Your final score is : ",flag)
        print("THANK YOU!!! for playing ")
        break