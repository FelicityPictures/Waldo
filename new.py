import google, urllib2, re, bs4

stoptext = open("stop.txt", 'r')

def cutQuery(q_words = []):
    counter = 0
    while counter<len(q_words):
        print "counter" + str(counter)
        with open('stop.txt') as f:
            for word in f:
                print ". " + word + " ."
		print type(word)
		print type(q_words[counter])
		print str(word) + " =?= " + q_words[counter]
                if word == q_words[counter]:
                    q_words[counter] = ''
        counter = counter+1
    r = " ".join(q_words)
    print r
    return str(r) # string of words to query


def search(query = ""):
    q_words = query.lower().split(' ')
    print "q_words: " + str(q_words)
    search_q = cutQuery(q_words)
    print "new query: " + search_q
    firstWord = q_words[0]
    print "firstWord: " + str(firstWord)

    if firstWord == "who":
        print "who" #do this
    elif firstWord == "what":
        print "what" #do this
    elif firstWord == "when":
        print "when" # do this
    elif firstWord == "where":
        print "where" # do this

cutQuery(['who', 'is', 'superman?'])
#search("What is Superman?")


