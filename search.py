import google, urllib2, bs4, re

x = 0

#decides what kind of question it is and how we will find the answer
def first(question = ""):
    global x
    first = question.split(' ', 1)[0].lower()
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
    return first

#gets results from google and turns into actual string
def getResults(question = ""):
    question = question.lower()
    

#breaks down string and returns real answer. Use this method only!
def answer(question = ""):
    

print first("Where am I?")+ str(x)
