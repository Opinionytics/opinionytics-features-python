# Popularity 
```
import json
from watson_developer_cloud.natural_language_understanding_v1 import Features ConceptsOptions
```
## Extract popularity from a text
```
def extractPopularityText(pytrends, natural_language_understanding, text,numberConcepts=4):
```

### Getting the concepts of the text
```
    response = natural_language_understanding.analyze(
        text=text,
        features=Features(concepts=ConceptsOptions(limit=numberConcepts)))
```
#### Parsing the json response
```
    concepts = response["concepts"]
    concepts = [k for k in concepts if k['relevance'] > 0.75]
```
### Google trends for getting the popularity of each concept
```
    kw_list = [k['text'] for k in concepts]
```
#### Timeframe indicates the period during which we mesure popularity
```    
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='',gprop='')
    data = pytrends.interest_over_time()
    data = data.drop('isPartial', axis=1)
```
#### Average popularity during the last month
```
    average = data.mean()
```
### Convert the results to json
```
    dict_averages = average.to_dict()
    result = json.dumps(dict_averages)
    print(result, '\n')
```
## Extract popularity from an URL
```
def extractPopularityUrl(pytrends, natural_language_understanding, url,numberConcepts=4):

    response = natural_language_understanding.analyze(
        url=url,
        features=Features(concepts=ConceptsOptions(limit=numberConcepts)))

    concepts = response["concepts"]
    concepts = [k for k in concepts if k['relevance'] > 0.75]


    kw_list = [k['text'] for k in concepts]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 1-m', geo='', gprop='') 
    data = pytrends.interest_over_time()
    data = data.drop('isPartial', axis=1)

    average = data.mean()

    dict_averages = average.to_dict()
    result = json.dumps(dict_averages)
    print(result, '\n')
```
## Extract popularity from data
```
def extractPopularityData(pytrends, natural_language_understanding, data,numberConcepts=4):
    for text in data:
        extractPopularityText(pytrends, natural_language_understanding,text.get('text'), numberConcepts)
```
