"""TIC TAC TOE GAME
Name Ansh Gupta
CSE AIML B2
SAP ID 500075765
Roll 35"""

lst=["0","1","2","3","O","5","6","7","8"]     
def show():
    print("|",lst[0],"|",lst[1],"|",lst[2],"|")
    print("-------------")
    print("|",lst[3],"|",lst[4],"|",lst[5],"|")
    print("-------------")
    print("|",lst[6],"|",lst[7],"|",lst[8],"|")
    print("*************")
show()
i=1
while True:
    if(i%2!=0):
        print("Chance of X")
        spot=int(input("Enter a spot\n"))
        if 0>spot>8 or lst[spot]=="O" or lst[spot]=="X" or spot==4:
            print("Spot cannot be taken")
            continue
        else:
            lst[spot]="X"
    else:
        print("Chance of O")
        spot=int(input("Enter a spot\n"))
        if 0>spot>8 or lst[spot]=="O" or lst[spot]=="X" or spot==4:
            print("Spot cannot be taken")
            continue
        else:
            lst[spot]="O"
    show()
    if(lst[0]==lst[1]==lst[2] or lst[0]==lst[3]==lst[6] or lst[0]==lst[4]==lst[8] or lst[2]==lst[5]==lst[8] or lst[6]==lst[7]==lst[8] or lst[2]==lst[4]==lst[6] or lst[0]==lst[3]==lst[6] or lst[3]==lst[4]==lst[5] or lst[1]==lst[4]==lst[7]):
        if(i%2!=0):
            print("X Wins!!!!!")
            print("Game Over")
            break
        else:
            print("0 Wins!!!!!")
            print("Game Over")
            break
    i=i+1
    if i==8:
        print("Its a tie.......No one wins")
        print("Game Over")
        break
    
