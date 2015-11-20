import google, urllib2, bs4, re

x = 0
q = ""

#decides what kind of question it is and how we will find the answer
#removes stop words from question and change into q, which we will google
def first(question = ""):
    global x, q
    first = question.split(' ',1)[0].lower()
    #changes x
    if first == 'who':
        x = 1
    elif first == 'what':
        x = 2
    elif first == 'when':
        x = 3
    elif first == 'where':
        x = 4
    elif first == 'why':
        x = 5
    elif first == 'is':
        x = 6
    elif first == 'how':
        x = 7
    elif first == 'which':
        x = 8

    #changes q, removes stopwords
    for w in question:
        if:
            

#gets results from google and returns string without stopwords
def getResults(question = ""):
    question = question.lower()
    

#breaks down string and returns real answer. Use this method only!
def answer(question = ""):
    

print first("Where am I?")+ str(x)
