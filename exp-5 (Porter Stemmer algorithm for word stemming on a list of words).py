import nltk
from nltk.stem import PorterStemmer
porter_stemmer = PorterStemmer()
words = ["running", "jumps", "easily", "fairly", "studies", "cats"]
stemmed_words = [porter_stemmer.stem(word) for word in words]
for word, stemmed in zip(words, stemmed_words):
    print(f"Original: {word} -> Stemmed: {stemmed}")
