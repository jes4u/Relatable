import spacy
import pytextrank

from bs4 import BeautifulSoup
from googlesearch import search
import requests

# input should come from GET request param
input = 'https://hackernoon.com/top-python-web-development-frameworks-to-learn-in-2019-21c646a09a9a'
text = requests.get(input).text

soup = BeautifulSoup(text, 'lxml')
text = soup.get_text()

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load('en_core_web_sm')

# add PyTextRank to the spaCy pipeline
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

# ML NLP AI magic
doc = nlp(text)

# examine the top-ranked phrases in the document
# concatenate unique words from phrases to make search query
textSet = {}
textList = []
i = 0
for p in doc._.phrases:
    for word in str.split(p.text):
        if word not in textSet and i < 10:
            # print(word)
            textSet[word] = 1
            textList.append(word)
    i += 1

query = ' '.join(textList)
print(query)

resultList = []
for result in search(query, tld='com', lang='en', num=5, start=0, stop=20, pause=0):
    print(result)

# result added to JSON to be returned from request
