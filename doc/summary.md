# Summary Feature

## Summarize a text input

### Summarize text input with sentences number
```
def summaryTextToSentences(client, text, title, SENTENCES_NUMBER):
    summary = client.Summarize({'text': text, 'title': title, 'sentences_number': SENTENCES_NUMBER})
    for sentence in summary['sentences']:
        print("{ %s }" %sentence, '\n')
```
### Summarize text input with sentences percentage
```
def summaryTextToPercentage(client, text, title, SENTENCES_PERCENTAGE):
    summary = client.Summarize({'text': text, 'title': title, 'sentences_percentage': SENTENCES_PERCENTAGE})
    for sentence in summary['sentences']:
        print("{ %s }" %sentence, '\n')
```
## Summarize an URL input

### Summarize an URL input with sentences number
```
def summaryUrlToSentences(client, url, SENTENCES_NUMBER):
    summary = client.Summarize({'url': url, 'sentences_number': SENTENCES_NUMBER})
    for sentence in summary['sentences']:
        print("{ %s }" %sentence, '\n')
```
### Summarize an URL input with sentences percentage
```
def summaryUrlToPercentage(client, url, SENTENCES_PERCENTAGE):
    summary = client.Summarize({'url': url, 'sentences_percentage': SENTENCES_PERCENTAGE})
    for sentence in summary['sentences']:
        print("{ %s }" %sentence, '\n')
```
## Summarize a JSON input

### Summarize JSON input with sentences number
```
def summaryDataToSentences(client, data, SENTENCES_NUMBER):
    for text in data:
        summaryTextToSentences(client, text.get('text'), text.get('title'), SENTENCES_NUMBER)
```        
### Summarize JSON input with sentences number
```
def summaryDataToPercentage(client, data, SENTENCES_PERCENTAGE):
    for text in data:
        summaryTextToPercentage(client, text.get('text'), text.get('title'), SENTENCES_PERCENTAGE)
```