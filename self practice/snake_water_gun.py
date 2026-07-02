import random
computer=random.choice([1,-1,0])
you=input("enter the choice")
youstr={"s":1,"w":-1,"g":0}
rev={1:"snake",-1:"water",0:"gun"}
your=youstr[you]
print(f"your choice is{rev[your]} and computer choice is {rev[computer]}")
if (computer==your):
    print("draw")
else:
    if your==1 and computer==-1:#snake water
        print("you win")
        
    elif your==1 and computer==0:#snake and gun

        print("computer win")
        
    elif your==-1 and computer==0:#water and gun
        print("computer win")
    else:
        print("wrong choice")
