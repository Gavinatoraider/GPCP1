#Gavin Pierce, Graded Quiz

four= input("does 2+2=4? ")

CentsInADollar=input("is there 1000 cents in a dollar? ")

areYouLiving=input("are you Living? (the answer should be yes.) " )

didYouGetGood=input("did you get good " )

earthOK=input("is the earth exploded " )

score = 0

if four == "yes": score += 1

if CentsInADollar == "no": score += 1

if areYouLiving == "yes": score += 1

if didYouGetGood == "yes": score += 1

if earthOK == "no": score += 1

print("you got", score, "out of five")