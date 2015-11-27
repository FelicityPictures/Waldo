import google, urllib2, re, bs4

stoptext = open("stop.txt", 'r')

def subjectofQ(q_words = []):
    counter = 0
    while counter<len(q_words):
        with open('stop.txt') as f:
            for word in f:
                if q_words[counter]==word:
                    q_words.remove(counter)
        counter = counter+1
    r = " ".join(q_words)
    print type(r)
    x = "hello"
    print type(x)
    return str(r) # string of words to query


def search(query = ""):
    q_words = query.lower().split(' ')
    print "q_words: " + str(q_words)
    subjectOfQ = subjectofQ(q_words)
    print "subjectofQ: " + str(subjectofQ)
    firstWord = q_words[0]
    print "firstWord: " + str(firstWord)

    if firstWord == "who":
        #do this
    elif firstWord == "what":
        #do this
    elif firstWord == "when":
        # do this
    elif firstWord == "where":
        # do this

search("What is Superman?")

