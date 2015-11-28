import google, urllib2, re, bs4

stoptext = open("stop.txt", 'r')

def cutQuery(q_words = []):
    counter = 0
    while counter<len(q_words):
        q_words[counter] = re.sub(r'[^\w\s]','',q_words[counter])
        with open('stop.txt') as f:
            for word in f:
		word = word.strip('\n')
                if word == q_words[counter]:
                    q_words[counter] = ''
        counter = counter+1
    r = " ".join(q_words).strip()
    return r # string of words to query


def search(query = ""):
    q_words = query.lower().split(' ')
    search_q = cutQuery(q_words)
    firstWord = "." + q_words[0]
    print "firstWord: " + str(firstWord)

    if firstWord == "who":
        print "who" #do this
    elif firstWord == "what":
        print "what" #do this
    elif firstWord == "when":
        print "when" # do this
    elif firstWord == "where":
        print "where" # do this

#cutQuery(['Who.', 'is.', ',Superman?'])
search("What. is, !Superman?")


