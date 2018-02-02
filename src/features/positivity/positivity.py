# Positivity Feature

## Having the Positivity from text input

def textPositivity(client, text):
    sentiment = client.Sentiment({"text": text})
    del sentiment['text'], sentiment['subjectivity'], sentiment['subjectivity_confidence']
    print(sentiment, '\n')

## Having the Positivity from url input

def urlPositivity(client, url):
    sentiment = client.Sentiment({"url": url}) 
    del sentiment['text'], sentiment['subjectivity'], sentiment['subjectivity_confidence']
    print(sentiment, '\n')

## Having the Positivity from JSON input

def dataPositivity(client, data):
    for text in data:
        textPositivity(client, text.get('text')) 