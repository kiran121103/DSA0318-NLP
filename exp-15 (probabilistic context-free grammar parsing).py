import nltk
from nltk import PCFG
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | Det N PP [0.5]
    VP -> V NP [0.5] | V NP PP [0.5]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.5] | 'dog' [0.5]
    V -> 'chases' [0.5] | 'sees' [0.5]
    P -> 'with' [0.5] | 'without' [0.5]
""")
parser = nltk.ViterbiParser(grammar)
sentence = "the cat chases the dog".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    print(f"Probability: {tree.prob()}")
