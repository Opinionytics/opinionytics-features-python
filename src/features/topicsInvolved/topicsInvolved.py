# Topics Involved Feature

## Classifying text from a string input 

def classifyText(client, text):
    classifications = client.Classify({"text": text}) 
    for category in classifications['categories']:
        print(category, '\n')

## Classifying Text from An URL

def classifyUrl(client, url):
    classifications = client.Classify({"url": url}) 
    for category in classifications['categories']:
        print(category, '\n')

## Classifying data from a file input

def classifyData(client, data):
    for text in data:
        classifyText(client, text.get('text')) 

