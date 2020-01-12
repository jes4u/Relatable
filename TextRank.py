import spacy
import pytextrank

from bs4 import BeautifulSoup
from googlesearch import search
import requests


import json


# input should come from GET request param

def textToQuery(input):
    # load a spaCy model, depending on language, scale, etc.
    nlp = spacy.load('en_core_web_sm')

    # add PyTextRank to the spaCy pipeline
    tr = pytextrank.TextRank()
    nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

    # ML NLP AI magic
    doc = nlp(input)

    # examine the top-ranked phrases in the document
    # concatenate unique words from phrases to make search query
    textSet = {}
    textList = []
    i = 0
    for p in doc._.phrases:
        for word in str.split(p.text):
            if word not in textSet and i < 10:
                textSet[word] = 1
                textList.append(word)
        i += 1

    query = ' '.join(textList)

    resultList = []
    for url in search(query, tld='com', lang='en', num=5, start=0, stop=5, pause=0):
        resultList.append(url)

    titleList = []

    from time import sleep

    for url in resultList:
        html = requests.get(url).text
        newSoup = BeautifulSoup(html, 'lxml')
        titleList.append(newSoup.title.text)

    object = {'keywords': textList,
              'pages': resultList,
              'titles': titleList}
    print(object)
    print()

    return json.dumps(object)


def htmlToQuery(html):
    soup = BeautifulSoup(html, 'lxml')
    text = soup.get_text()
    return textToQuery(text)

def urlToQuery(url):
    html = requests.get(url).text
    return htmlToQuery(html)

# def keywordsToQuery(url):




from flask import Flask
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/query/', methods=['GET', "POST"])
def query():
    try:
        if request.method == "GET":
            response = app.response_class(
                response=urlToQuery(request.args.get('url')),
                mimetype='application/json'
            )
            return response
        elif request.method == "POST":
            response = app.response_class(
                response=htmlToQuery(request.args.get('text')),
                mimetype='application/json'
            )
            return response

    except Exception as e:
        return ''
