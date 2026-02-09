import nltk
from nltk.corpus import brown

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

cfd.tabulate(
    conditions=['government', 'humor', 'reviews'],
    samples=['leadership', 'worship', 'hardship']
)

cfd.plot(
    conditions=['government', 'humor', 'reviews'],
    samples=['leadership', 'worship', 'hardship']
)

news_fd = cfd['news']
print(news_fd.most_common(3))
print(news_fd['the'])
