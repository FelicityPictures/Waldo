import google, urllib2, re, bs4

stoptext = open("stop.txt", 'r')

#Takes question and removes stop words to get the subject of the question
#that will be used for googling
def question(question = ""):
    question = question.lower().split(" ")
    counter = 0
    while counter<len(question):
        with open('stop.txt') as f:
            for word in f:
                if word.replace('\n', '') == question[counter]:
                    question[counter] = ""
        counter = counter + 1
    r = " ".join(question).strip()
    return r

print question("Who is Superman")
