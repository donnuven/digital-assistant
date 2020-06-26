import wolframalpha
from config import *


def wolfram_api():
    '''
    wolfram api usage sample

    '''

    client = wolframalpha.Client(data['WOLFRAM_ID'])

    query = str(input('input: '))
    res = client.query(query)
    results = next(res.results).text
    print(results)
