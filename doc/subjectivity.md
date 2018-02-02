# Positivity Feature

## Having the Subjectivity from text input
```
def textSubjectivity(client, text):
    sentiment = client.Sentiment({"text": text})
    del sentiment['text'], sentiment['polarity'], sentiment['polarity_confidence']
    print(sentiment, '\n')
```
## Having the Subjectivity from URL input
```
def urlSubjectivity(client, url):
    sentiment = client.Sentiment({"url": url}) 
    del sentiment['text'], sentiment['polarity'], sentiment['polarity_confidence']
    print(sentiment, '\n')
```
## Having the Subjectivity from JSON input
```
def dataSubjectivity(client, data):
    for text in data:
        textSubjectivity(client, text.get('text')) 
```