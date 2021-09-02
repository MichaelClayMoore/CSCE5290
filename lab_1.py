# imports for code
from bs4 import BeautifulSoup
import urllib.request
import nltk
from nltk.corpus import stopwords

# reads the wiki for spacex
response = urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()

# parses the html and gets the text
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)

# gets the words from the text
tokens = [t for t in text.split()]
clean_tokens = tokens[:]

# remove stopwords and numbers from the text
sr = stopwords.words('english')
for token in tokens:

    # removes stopwords
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
    
    try:
        int(token)
        clean_tokens.remove(token)
    except:
        continue

# make a freqDist class for our words
freq = nltk.FreqDist(clean_tokens)

# get all the word-freq pair
all_words = list(freq.items())

# filter words less than 5
all_words_filter = list(filter(lambda x: x[1]>5, all_words))

# put them all back into a list
# this is done to recreate the freqDist class
all_words = []
for pair in all_words_filter:
    all_words.extend([pair[0]] * pair[1])

# create freqDist class
freq = nltk.FreqDist(all_words)

# plot the most frequent words
freq.plot(10, cumulative=False)

# import plt to do a bar chart
import matplotlib.pyplot as plt

# sort the words to get the same results as above
all_words_filter.sort(key=lambda x: x[1], reverse=True)

# x and y for graph
words = [w[0] for w in all_words_filter]
val = [w[1] for w in all_words_filter]

# plot graph
# plt.bar(words[:10], val[:10])
# plt.show()
