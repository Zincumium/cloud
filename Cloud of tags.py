f = open('D:/text.txt', "r", encoding="utf-8")
text = f.read()
len(text)
text[:500]
text = text.lower()
import string
print(string.punctuation)
symbols = string.punctuation + '/|\.,()-_=+%<>'
def delete_symbols(text, symbols):
    return "".join([ch for ch in text if ch not in symbols])
text = delete_symbols(text, symbols)
text = delete_symbols(text, string.digits)
import nltk
from nltk import word_tokenize 
text_token = word_tokenize(text)
len(text_token)
text_token[:10]
text = nltk.Text(text_token)
print(type(text))
text[:10]
from nltk.probability import FreqDist
fdist = FreqDist(text)
fdist.most_common(5)
fdist.plot(30,cumulative=False)
from nltk.corpus import stopwords
russian_stopwords = stopwords.words("russian")
print(len(russian_stopwords))
from wordcloud import WordCloud
import matplotlib.pyplot as plt
text_raw = " ".join(text)
wcloud = WordCloud().generate(text_raw)
plt.imshow(wcloud)
plt.axis('off')
plt.show()
wcloud.to_file('test.jpg')
