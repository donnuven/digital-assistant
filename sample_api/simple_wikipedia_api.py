import wikipedia

'''
This is a wikipedia API usage sample.

'''
query = str(input('input: '))
wikipedia.summary(query)
print(wikipedia.summary(query))
