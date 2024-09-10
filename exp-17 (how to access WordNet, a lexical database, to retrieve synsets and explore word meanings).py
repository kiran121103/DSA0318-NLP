from nltk.corpus import wordnet

def explore_word_meanings(word):
    synsets = wordnet.synsets(word)
    
    if not synsets:
        print(f"No synsets found for '{word}'")
        return
    
    print(f"Synsets for '{word}':")
    for synset in synsets:
        print(f"\tDefinition: {synset.definition()}")
        print(f"\tExamples: {synset.examples()}")
        print()

if __name__ == "__main__":
    word = input("Enter a word to explore its meanings: ")
    explore_word_meanings(word)
