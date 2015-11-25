
import google, urllib2, re, bs4

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
    counter = 0
    while counter < len(first):
        with open('stop.txt') as f:
            for word in f:
                if first[counter] == word:
                    first.remove(counter)
        counter += 1
        
    cleanQuestion = ""
    for w in first:
        cleanQuestion += w + ' ' 

    print "x = " + str(x)
    return cleanQuestion
    
print first("What is Superman?")
            
"""
#gets results from google and returns string without stopwords
def getResults(question = ""):

    global x
    #for when the question starts with a who
    #searches through google results for names
    if x==1:
        nameDictionary = {}
        results = google.search(question,num=5 ,start=0,stop=5 )
        urls = []
        for r in results:
            urls.append(r)
#           results = []
            counter = 0
            while counter < len(urls):
                url=urllib2.urlopen(urls[counter])
                page = url.read().decode('utf-8')
                soup = bs4.BeautifulSoup(page, "html.parser")
                raw = soup.get_text(page)
                text = re.findAll("[\t\n ]+",' ',raw[0:300])
                results.append(text)
                counter += 1

        #loop through nameDictionary to find the one with highest entry
        return
    #for when the question starts with a what
    #gets photos from google
    elif x==2:

    results = google.search(question,num=5 ,start=0,stop=5 )
   
    urls = []
    for r in results:
        print r
        urls.append(r)

    results = []
    counter = 0
    while counter < len(urls):
        url=urllib2.urlopen(urls[counter])
        page = url.read().decode('utf-8')
        soup = bs4.BeautifulSoup(page, "html.parser")
        raw = soup.get_text(page)
        text = re.findAll("[\t\n ]+",' ',raw[0:300])
        results.append(text)
        counter += 1

    return urls
      
    

print getResults("Who is Superman?")

"""
