import google, urllib2, bs4, re

x = 0
q = ""

stoptext = open("stop.txt",'r')

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
    word = 0
    
    while word < len(question):
        with open('stop.txt') as f:
            for stopWord in f:
                print stopWord
                if word == stopWord:
                    word +=2
                    #will add a way to remove the word
                    #what is question? a list? or a string?
        word += 1
    return question
    
                    
            

#gets results from google and returns string without stopwords
def getResults(question = ""):
    results = google.search(question,num=20,start=0,stop=20)
   
    urls = []
    for r in results:
        urls.append(r)
    
    counter = 0
    while counter < len(urls):
        url=urllib2.urlopen(urls[counter])
        page = url.read().decode('utf8')
        soup = bs4.BeautifulSoup(page, "html.parser")
        raw = soup.get_text(page)
        text = re.sub("[\t\n ]+",' ',raw)
        urls[counter] = text

    return urls
        
    
    
    

#breaks down string and returns real answer. Use this method only!
#def answer(question = ""):
    

#print getResults("superman")
