import google, urllib2, re, bs4

stoptext = open("stop.txt", 'r')

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
    return r # string of words to query

def getResults(query, regex):
    results = google.search(query,num=2,start=0,stop=2 )
   
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
        text = re.search(regex, raw[0:400])
        results.append(text)
        counter += 1
    return results


def search(query):
    q_words = query.lower().split(' ')
    q_type = re.sub(r'[^\w\s]','',q_words[0])
    print "q_type: " + q_type
    search_q = cutQuery(q_words)
    print "search_q: " + search_q

    if q_type == "who":
        getResults(query, "([A-Z]{?}) ([a-z]{7})")
    elif q_type == "what":
        print "what" #do this
    elif q_type == "when":
        print "when" # do this
    elif q_type == "where":
        print "where" # do this
    else:
        print "invalid search please try again"

search("Who is Clark Kent")

