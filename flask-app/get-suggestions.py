from bs4 import BeautifulSoup
import requests
import spacy
import pytextrank
from googlesearch import search
import json



def getBodyText(webURL):
    # beautiful soup
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

def urlToQuery(url):
    bodyText = getBodyText(url)

    queryList = getTextRank(bodyText)
    googleSearched = googling(' '.join(queryList))

    resultDict = {}
    resultDict["keywords"] = queryList
    resultDict["pages"] = googleSearched

    app_json = json.dumps(resultDict)

    return app_json


from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/query/', methods=['GET'])
def query():
    if request.method == "GET":
        response = app.response_class(
            response=urlToQuery(request.args.get('url')),
            mimetype='application/json'
        )
        return response
