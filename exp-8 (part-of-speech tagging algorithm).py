from collections import defaultdict

training_data = [
    ('The', 'DT'), ('dog', 'NN'), ('barks', 'VB'),
    ('A', 'DT'), ('cat', 'NN'), ('meows', 'VB'),
    ('The', 'DT'), ('cat', 'NN'), ('sleeps', 'VB')
]

word_tag_counts = defaultdict(lambda: defaultdict(int))
tag_counts = defaultdict(int)

for word, tag in training_data:
    word_tag_counts[word][tag] += 1
    tag_counts[tag] += 1

def get_most_likely_tag(word):
    if word in word_tag_counts:
        return max(word_tag_counts[word], key=word_tag_counts[word].get)
    return 'NN'  

sentence = "The dog sleeps"
words = sentence.split()

tagged_sentence = [(word, get_most_likely_tag(word)) for word in words]

print("Tagged Sentence:", tagged_sentence)
