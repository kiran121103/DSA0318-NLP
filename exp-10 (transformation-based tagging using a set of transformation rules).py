import nltk
from nltk.tag import RegexpTagger

text = "The quick brown fox jumps over the lazy dog"

tokens = nltk.word_tokenize(text)
patterns = [
    (r'.*s$', 'NNS'),  
    (r'.*', 'NN')      
]

tagger = RegexpTagger(patterns)

tagged_tokens = tagger.tag(tokens)

print(tagged_tokens)
