# Opinionytics v0.1

## Util Imports 

import sys 
import os
import json

## Importing APIs 

from aylienapiclient import textapi
from pytrends.request import TrendReq 
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, ConceptsOptions

## Importing Packages

### Topics Involved Feature Feature

topicsInvolvedPath = "src/features/topicsInvolved"
sys.path.insert(0, topicsInvolvedPath)
from topicsInvolved import *

### Summary Feature

summaryPath = "src/features/summary"
sys.path.insert(0, summaryPath)
from summary import *

### Positivity Feature

positivityPath = "src/features/positivity"
sys.path.insert(0, positivityPath)
from positivity import *

### Subjectivity Feature

subjectivityPath = "src/features/subjectivity"
sys.path.insert(0, subjectivityPath)
from subjectivity import *  

### Popularity Feature

popularityPath = "src/features/popularity"
sys.path.insert(0, popularityPath)
from popularity import *

## Aylien API Keys

APP_ID = "8ebd4c0e"
APP_KEY = "707f70d4fe70e4e22210bfd824949ba9"

## Watson API Keys

USERNAME='ea1c5c7c-c39e-4af6-bcd5-b9103dc229a2'
PASSWORD='Xl21Xq1EeDwW'
VERSION='2017-02-27'

## Connexion to the APIs

client = textapi.Client(APP_ID, APP_KEY)

natural_language_understanding = NaturalLanguageUnderstandingV1(
    username=USERNAME,
    password=PASSWORD,
    version=VERSION)

## Initialize google trends

pytrends = TrendReq(hl='en-US', tz=360)

## Query Params

text = """Maximilian Karl Emil "Max" Weber (21 April 1864 – 14 June 1920) was a German sociologist, philosopher, jurist, and political economist. His ideas profoundly influenced social theory and social research. Weber is often cited, with Émile Durkheim and Karl Marx, as among the three founders of sociology.Weber was a key proponent of methodological antipositivism, arguing for the study of social action through interpretive (rather than purely empiricist) means, based on understanding the purpose and meaning that individuals attach to their own actions. Unlike Durkheim, he did not believe in monocausality and rather proposed that for any outcome there can be multiple causes.

Weber's main intellectual concern was understanding the processes of rationalisation, secularisation, and "disenchantment" that he associated with the rise of capitalism and modernity.He saw these as the result of a new way of thinking about the world. Weber is best known for his thesis combining economic sociology and the sociology of religion, elaborated in his book The Protestant Ethic and the Spirit of Capitalism, in which he proposed that ascetic Protestantism was one of the major "elective affinities" associated with the rise in the Western world of market-driven capitalism and the rational-legal nation-state. He argued that it was in the basic tenets of Protestantism to boost capitalism. Thus, it can be said that the spirit of capitalism is inherent to Protestant religious values.

"""

title = "Max Weber"

url = "http://techcrunch.com/2015/04/06/john-oliver-just-changed-the-surveillance-reform-debate"

SENTENCES_NUMBER = 1

SENTENCES_PERCENTAGE = 15

### JSON File

_jsonFile = 'src/resources/random_texts.json'
_jsonData = open(_jsonFile, 'r')
data = json.load(_jsonData)

## Text Classification - Topics Involved

classifyText(client, text)

## Url Classification - Topics Involved

classifyUrl(client, url)

## Data Classification - Topics Involved

classifyData(client, data)

## Text Summary with sentences number

summaryTextToSentences(client, text, title, SENTENCES_NUMBER)

## Text Summary with sentences penrcentage

summaryTextToPercentage(client, text, title, SENTENCES_PERCENTAGE)

## URL Summary with sentences number

summaryUrlToSentences(client, url, SENTENCES_NUMBER)

## URL Summary with sentences penrcentage

summaryUrlToPercentage(client, url, SENTENCES_PERCENTAGE)

## Data Summary with sentences number

summaryDataToSentences(client, data, SENTENCES_NUMBER)

## Data Summary with sentences penrcentage

summaryDataToPercentage(client, data, SENTENCES_PERCENTAGE)

## Text Positivity

textPositivity(client, text)

## URL Positivity

urlPositivity(client, url)

## Data Positivity

dataPositivity(client, data)

## Text Subjectivity

textSubjectivity(client, text)

## URL Subjectivity

urlSubjectivity(client, url)

## Data Subjectivity

dataSubjectivity(client, data)

## Text Popularity

extractPopularityText(pytrends, natural_language_understanding, text)

## URL Popularity

extractPopularityUrl(pytrends, natural_language_understanding, url)

## Data Popularity

extractPopularityData(pytrends, natural_language_understanding, data)