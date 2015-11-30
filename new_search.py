import google, urllib2, re, bs4

stoptext = open("stop.txt", 'r')

#Takes question and removes stop words to get the subject of the question
#that will be used for googling
def cutQuery(q_words):
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
    return r

def getResults(query, regex):
    results = google.search(query,num=2,start=0,stop=2)
   
    urls = []
    for r in results:
        urls.append(r)

    results = []
    counter = 0
    while counter < len(urls):
        url=urllib2.urlopen(urls[counter])
        page = url.read().decode('utf-8')
        soup = bs4.BeautifulSoup(page, "html.parser")
        raw = soup.get_text(page)
        results = re.search(regex, raw[0:2000])
      #  temp = re.search(regex, raw[0:2000])
      #  if temp is not None:
     #       text = temp.group(0)
     #   else:
     #       text = ""
    #    results.append(text)
     #   counter += 1
    return results


def search(query):
    q_words = query.lower().split(' ')
    q_type = re.sub(r'[^\w\s]','',q_words[0])
    print "q_type: " + q_type
    search_q = cutQuery(q_words)
    print "search_q: " + search_q

    if q_type == "who":
        #Only finds names (ALL names)
        reg = "((" + search_q + " is) ([A-Z]{1}[a-z]*)?)"
        return getResults(query, reg)

    elif q_type == "what":
        return []

    elif q_type == "when":
        #Only finds dates in the format of:
        #<dayOfWeek>, <Month> <dayOfMonth>, <Year>
        reg = "((" + search_q + " is on) (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), ?(January|February|March|April|May|June|July|August|September|October|November|December) [0-9]{1,2}, [0-9]{4})"
        return getResults(query, reg)

    elif q_type == "where":
        #Only works on <place1>, <place2>
        reg = "((" + search_q + " is in) ((([A-Z]{1}[a-z]*) ([A-Z]{1}[a-z]*)), ([A-Z]{2}|[A-Z]{1}[a-z]* [A-Z]{1}[a-z]*)))"
        return getResults(query, reg)
    else:
        return []

#search("Who is Clark Kent")

