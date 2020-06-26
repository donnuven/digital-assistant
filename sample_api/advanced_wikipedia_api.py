import wikipedia
'''
This is a wikipedia API usage sample.

 '''

query = str(input('input: '))
wikipedia.summary(query, sentences=4)
print(wikipedia.summary(query, sentences=4))
