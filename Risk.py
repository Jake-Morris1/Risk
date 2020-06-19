# Risk
# 20-05-2020
# Jake Morris

import random
import time


attacking="y"


print("Hello. Player 1 is attacking and Player 2 is defending.")

while attacking=="y":
    end=""
    armiesP1=1
    armiesP2=0
    diceP1=0
    counterP1=0
    counterP2=0
    P1Rolls=[]
    P2Rolls=[]
    while armiesP1<2:
        armiesP1=int(input("\nHow many armies are on Player 1's territory? "))
        if armiesP1==1:
            print("\nPlayer 1 can not attack from that territory!")
        elif armiesP1<1:
            print("\nThat is an invalid amount of armies!")
    while armiesP2<1:
        armiesP2=int(input("\nHow many armies are on Player 2's territory? "))
        if armiesP2<1:
            print("\nThat is an invalid amount of armies!")
        elif armiesP2>=2:
            diceP2=2
        else:
            diceP2=1


    while diceP1<1 or diceP1>3 or diceP1>=armiesP1:
        diceP1=int(input("\nHow many dice does Player 1 want to attack with? "))
        if diceP1<1 or diceP1>3:
            print("\nThat is an invalid amount of dice!")
        elif diceP1>=armiesP1:
            print("\nYou cannot use that many dice on that territory!")

    while counterP1!=diceP1:
        P1Num=random.randint(1,6)
        P1Rolls.append(P1Num)
        print("\nPlayer 1 rolls a...\n")
        time.sleep(1.5)
        print(P1Num)
        time.sleep(1)
        counterP1=counterP1+1

    while counterP2!=diceP2:
        P2Num=random.randint(1,6)
        P2Rolls.append(P2Num)
        print("\nPlayer 2 rolls a...\n")
        time.sleep(1.5)
        print(P2Num)
        time.sleep(1)
        counterP2=counterP2+1

    if diceP1==1 and diceP2==1:
        P1Num1=P1Rolls[0]
        P2Num1=P2Rolls[0]
        if P1Num1>P2Num1:
            print("\nPlayer 1 wins.")
            print("\nPlayer 2 lost 1 army!")
            print("\nPlayer 1 has conquered that territory!")
        else:
            print("\nPlayer 2 wins.")
            if armiesP1==2:
                print("\nPlayer 1 can no longer attack from that territory!")
                
    elif diceP1==2 and diceP2==1:
        P1Num1=P1Rolls[0]
        P1Num2=P1Rolls[1]
        P2Num1=P2Rolls[0]
        if P1Num1>P2Num1 or P1Num2>P2Num1:
            print("\nPlayer 1 wins.")
            print("\nPlayer 1 has conquered that territory!")
        else:
            print("\nPlayer 2 wins.")
            print("\nPlayer 1 lost 1 army!")
    elif diceP1==3 and diceP2==1:
        P1Num1=P1Rolls[0]
        P1Num2=P1Rolls[1]
        P1Num3=P1Rolls[2]
        P2Num1=P2Rolls[0]
        if P1Num1>P2Num1 or P1Num2>P2Num1 or P1Num3>P2Num1:
            if P2Num1>=P1Num1 and P2Num1>=P1Num2 and P1Num1>P2Num1:
                print("\nPlayer 1 lost 1 army!")
            if P2Num1>=P1Num1 and P2Num1>=P1Num3 and P1Num2>P2Num1:
                print("\nPlayer 1 lost 1 army!")
            if P2Num1>=P1Num1 and P2Num1>=P1Num2 and P1Num3>P2Num1:
                print("\nPlayer 1 lost 1 army!")
            print("\nPlayer 1 wins.")
            print("\nPlayer 1 has conquered that territory!")
        else:
            print("\nPlayer 2 wins.")
            print("\nPlayer 1 lost 1 army!")
    elif diceP1==1 and diceP2==2:
        P1Num1=P1Rolls[0]
        P2Num1=P2Rolls[0]
        P2Num2=P2Rolls[1]
        if P1Num1>P2Num1 and P1Num1>P2Num2:
            print("\nPlayer 1 wins.")
            print("\nPlayer 2 lost 1 army!")
        else:
            print("\nPlayer 2 wins.")
            print("\nPlayer 1 lost 1 army!")
            if armiesP1==1:
                print("\nPlayer 1 can no longer attack from that territory!")
    elif diceP1==2 and diceP2==2:
        P1Num1=P1Rolls[0]
        P1Num2=P1Rolls[1]
        P2Num1=P2Rolls[0]
        P2Num2=P2Rolls[1]
        if P1Num1>P2Num1 or P1Num1>P2Num2 or P1Num2>P2Num1 or P1Num2>P2Num2:
            if P2Num1>=P1Num1 or P2Num1>=P1Num2 or P2Num2>=P1Num1 or P2Num2>=P1Num2:
                print("\nPlayer 1 lost 1 army!")
                print("\nPlayer 2 lost 1 army!")
            elif P1Num1>P2Num1 or P1Num1>P2Num2 and P1Num2>P2Num1 or P1Num2>P2Num2:
                print("\nPlayer 1 wins.")
                print("\n\Player 1 has conquered that territory!")
        else:
            print("\nPlayer 2 wins.")
            print("\nPlayer 1 lost 2 armies!")
            print("\nPlayer 1 can no longer attack from that territory!")
            
    elif diceP1==3 and diceP2==2:
        P1Num1=P1Rolls[0]
        P1Num2=P1Rolls[1]
        P1Num3=P1Rolls[2]
        P2Num1=P2Rolls[0]
        P2Num2=P2Rolls[1]
        if P1Num1>P2Num1 or P1Num1>P2Num2 or P1Num2>P2Num1 or P1Num2>P2Num2 or P1Num3>P2Num1 or P1Num3>P2Num2:
            if P1Num1>P2Num1 or P1Num1>P2Num2 and P1Num2>P2Num1 or P1Num2>P2Num2 and P1Num3>P2Num1 or P1Num3>P2Num2:
                print("\nPlayer 1 wins.")
                print("\nPlayer 2 lost 2 armies!")
                print("\nPlayer 1 has conquered that territory!")
            elif P1Num1>P2Num1 or P1Num1>P2Num2 and P2Num1>=P1Num2 or P2Num2>=P1Num2 and P2Num1>=P1Num3 or P2Num2>=P1Num3:
                print("\nPlayer 1 lost 1 army!")
                print("\nPlayer 2 lost 1 army!")
            elif P1Num2>P2Num1 or P1Num2>P2Num2 and P2Num1>=P1Num1 or P2Num2>=P1Num1 and P2Num1>=P1Num3 or P2Num2>=P1Num3:
                print("\nPlayer 1 lost 1 army!")
                print("\nPlayer 2 lost 1 army!")
            elif P1Num1>P2Num3 or P1Num1>P2Num3 and P2Num1>=P1Num1 or P2Num2>=P1Num1 and P2Num1>=P1Num2 or P2Num2>=P1Num2:
                print("\nPlayer 1 lost 1 army!")
                print("\nPlayer 2 lost 1 army!")
            elif P2Num1>=P1Num1 and P2Num1>=P1Num2 and P2Num1>=P1Num3 and P2Num2>=P1Num1 and P2Num2>=P1Num2 and P2Num2>=P1Num3:
                print("\nPlayer 1 lost 2 armies!")
                print("\nPlayer 2 wins!")
                
    while end!="y" and end!="n":
        end=input("\nWould Player 1 like to attack again? ")
        end=end.lower()
        if end=="y":
            attacking="y"
        elif end=="n":
            attacking="n"
        else:
            print("\nThat is an invalid option")

print("\n\nPlayer 1 has ended their turn!")












        
