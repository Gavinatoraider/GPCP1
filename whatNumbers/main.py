#Gavin Pierce,  What are these numbers?

comma =input("give me an integer with a number in thousands place ")
comma= int(comma)
decimal=input("give me a decimal 4 places ")
deciamal= float(decimal)
percentage=input("give me a percentage ")
percentage= float(percentage)
dollar=input("give a dollar amount ")
dollar= float(dollar)

commaPrint= "your number with commas is {:,}"

print(commaPrint.format(comma))
print("your float number is ",decimal)

percentagePrint= "your percent is {:%}"
print(percentagePrint.format(percentage))

print("you dollar amount is ", dollar)
