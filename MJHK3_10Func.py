#ends after 4 full circle
def fourCircle():

    #position of the round
    circle = 1
    banker = 1

    #players' current score
    score = [0,0,0,0]
    #seat
    seat = ["east","south","west","north"]
   
    while circle < 4 or banker < 4:
        
        #print info of current round
        print("circle = " + str(circle) + ", banker = " + str(banker))
        i = 0
        while i < 4:
            print (seat[i] + " = " + str(score[i]))
            i = i + 1
        
        #find out winner
        winner = winnerId()
        
        #if draw, move banker to next position and continue top loop
        if winner == 0:
            circle, banker = wind(circle, banker)
            continue

        score = addScore(winner, score)
        
        #ask if need to change banker
        change = changeBanker()
        
        if change =="y":
            circle, banker = wind(circle, banker)




################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#find out who won
def winnerId():
    
    #make sure input is integer
    while True:
        try:
            winner = input("which seat won? 0=draw,1=east,2=south,3=west,4=north: ")
            winner = int(winner)
            break
        except ValueError:
            print ("stop fucking around")
    
    #make sure input is in the range of 0:4
    if winner < 0 or winner > 4:
        print ("stop fucking around")
        winner = winnerID()
    
    return winner


################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#update score
def addScore(winner, score):
    
    #farn in integer
    farn = farnScore()
    #who needs to pay
    whoPay = whoPayMoney()
   
    #if conceded
    if whoPay != 0:
        payByOne = True
        whoBao = 0
    #self draw
    else:
        whoBao = bao()
    
        if whoBao == 0:
            payByOne = False
        else:
            payByOne = True

    #calculate payments
    payment(winner, farn, whoPay, payByOne, score, whoBao)

    return score
################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#how many farn
def farnScore():    

    while True:
        try:
            farn = input("how many farn? 3-10: ")
            farn = int(farn)
            break
        except ValueError:
            print ("stop fucking around")

    if farn < 3:
        print ("atleast 3 farn")
        farn = farnScore()
    
    if farn > 10:
        farn = 10

    return farn

################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#who pays
def whoPayMoney():

    while True:
        try:
            whoPay = input("who concede? 0=selfdraw,1=east,2=south,3=west,4=north: ")
            whoPay = int(whoPay)
            break
        except ValueError:
            print ("stop fucking around")

    if whoPay < 0 or whoPay > 4:
        print ("stop fucking around")
        whoPay = whoPayMoney()

    return whoPay

################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#if selfdraw, does someone need to pay for everyone
def bao():
    
    while True:
        try:
            bao = input("does someone need to bao? 0=no,1=east,2=south,3=west,4=north: ")
            bao = int(bao)
            break
        except ValueError:
            print ("stop fucking around")

    if bao < 0 or bao > 4:
        print ("stop fucking around")
        bao = bao()

    return bao

################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#calculate payment and update score
def payment(winner, farn, whoPay, payByOne, score, whoBao):
    
    #scoring system starting from 3 farn
    farnPoints = [0,0,0,8,16,32,48,64,96,128,256]
   
    amount = farnPoints[farn]
    
    if whoPay != 0:
        score[winner - 1] = score[winner - 1] + amount
        score[whoPay - 1] = score[whoPay - 1] - amount
    else:
        score[winner - 1] = score[winner - 1] + amount * 1.5
        if payByOne == True:
            score[whoBao - 1] = score[whoBao - 1] - amount * 1.5
        else:
            i = 0
            while i < len(score):
                if i != winner - 1:
                    score[i] = score[i] - amount * 0.5
                i = i + 1
            
################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#update banker and seat
def wind(circle, banker):
    
    if banker == 4:
        banker = 1
        circle = circle + 1
    else:
        banker = banker + 1

    return circle, banker
################################################################################################################################################
################################################################################################################################################
###############################################################################################################################################
#ask if change banker
def changeBanker():
    
    change = input("change banker? (y/n): ")
    
    if change != "y" and change != "n":
        print ("stop fucking around")
        change = changeBanker()

    return change

