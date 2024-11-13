# Gavin Pierce Secret Cypher

word=input("what is the word that you would like to use? ")
#empty string is mean to hold the values
cypher=""
def shift(word, cypher):
    for letter in word:
         #takes the word and converts it to numbers
        letter=ord(letter)
    #adds value
        letter+=1
        letter=chr(letter)
        #converts back to word
        cypher+=letter
    print(cypher)    

shift(word,cypher)

