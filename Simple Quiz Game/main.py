#Gavin Pierce Simple Quiz Game

name= input("whats your name? ")
score=0
print("now before you hand in your homework... ... ... POP QUIZ!!!!", name, "!!!!! Whats the answer? ")
questionOne= input("""qution what is 1+1
      A: 2
      B: 1
      C: 4
      D: 843528743653276532753290
                   """)
questionOneAnwers= ["2","1","4","843528743653276532753290"]

if questionOne in questionOneAnwers:
    if questionOne =="2":
        print("you got it right!")
        score+=1
    else: 
        print("no its wrong.  here is an easier problem ")
        easierQuestionOne= input("""what is 0 + 0
        A: 0
        B: 0
        C: 0
        D: 0
        """)
        easierQuestionOneAnswers= ["0"]
else:
    print("you gave invalid number")

questionTwo=input("""what is 5+5
    A: 5
    B: 10
    C: 550000000
    D: 55
                  """)
questionTwoAnwers=["5","10","550000000","55"]

if questionTwo in questionTwoAnwers:
    if questionTwo =="10":
        print("you got it right!")
        score+=1
    else: 
        print("no its wrong.  here is an easier problem ")
        easierQuestionOne= input("""what is 0 + 0
        A: 0
        B: 0
        C: 0
        D: 0
        """)
        easierQuestionOneAnswers= ["0"]
else:
    print("you gave invalid number")

questionThree=input("""what is 5*5
    A: 5
    B: 55
    C: 25
    D: 5500000000000
                    """)
questionThreeAnswers=["5","55","25","5500000000000"]

if questionThree in questionThreeAnswers:
    if questionThree =="25":
        print("you got it right!")
        score+=1
    else: 
        print("no its wrong.  here is an easier problem ")
        easierQuestionOne= input("""what is 0 + 0
        A: 0
        B: 0
        C: 0
        D: 0
        """)
        easierQuestionOneAnswers= ["0"]
else:
    print("you gave invalid number")

questionFour=input(""" what is 100*100
    A: 5
    B: 55
    C: 25
    D: 10000
                   """)
questionFourAnswers=["100","1000","10000","10000"]

if questionFour in questionFourAnswers:
    if questionFour =="10000":
        print("you got it right!")
        score+=1
    else: 
        print("no its wrong.  here is an easier problem ")
        easierQuestionOne= input("""what is 0 + 0
        A: 0
        B: 0
        C: 0
        D: 0
        """)
        easierQuestionOneAnswers= ["0"]
else:
    print("you gave invalid number")

questionFive=input("""what is the square root of 75984375937593
    A: 8716901.73959
    B: 87543
    C: 89354769
    D: 86484.908647
                   """)
questionFiveAnswers=["8716901.73959", "87543","89354769", "86484.908647"]

if questionFive in questionFiveAnswers:
    if questionFive =="8716901.73959":
        print("you got it right!")
        score+=1
    else: 
        print("no its wrong.  here is an easier problem ")
        easierQuestionOne= input("""what is 0 + 0
        A: 0
        B: 0
        C: 0
        D: 0
        """)
        easierQuestionOneAnswers= ["0"]
else:
    print("you gave invalid number")
print("your score is ", score )