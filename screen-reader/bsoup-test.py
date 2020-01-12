
def getBodyText(webURL):
    from bs4 import BeautifulSoup
    import requests

    # beautiful soup
    url = 'https://towardsdatascience.com/binary-tree-the-diameter-af2e9d725abe'
    r = requests.get(webURL, headers={'User-agent': 'your bot 0.1'})

    soup = BeautifulSoup(r.content, 'html.parser')

    paragraphs = list(soup.find_all('p'))

    # print(body.get_text())
    paragraphList = []
    paragraphs = soup.find_all('p')

    for pp in paragraphs:
        paragraphList.append(pp.get_text())

    joinedParagraphs = ' '.join(paragraphList)

    return joinedParagraphs


# text rank
def getTextRank(bodyText):
    import spacy
    import pytextrank

    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load("en_core_web_sm")

    # add PyTextRank to the spaCy pipeline
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    doc = nlp(bodyText)

    textRanked = []

    for p in doc._.phrases:
        textRanked.append(p.text)

    uniqueTerms = set(textRanked)

    return list(uniqueTerms)[:10]


# google search
def googling(term):
    from googlesearch import search

    query = term

    my_results_list = []
    for i in search(query,        # The query you want to run
                    tld = 'com',  # The top level domain
                    lang = 'en',  # The language
                    num = 5,     # Number of results per page
                    start = 0,    # First result to retrieve
                    stop = 20,  # Last result to retrieve
                    pause = 2.0,  # Lapse between HTTP requests
                   ):
        my_results_list.append(i)

    return my_results_list

url = 'https://towardsdatascience.com/binary-tree-the-diameter-af2e9d725abe'
bodyText = getBodyText(url)

queryList = getTextRank(bodyText)
# print(queryList)
googleSearched = googling(' '.join(queryList))



resultDict = {}
resultDict["keywords"] = queryList
resultDict["pages"] = googleSearched


# print(resultDict)