import nltk
from nltk import CFG
grammar=CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N -> 'cat'|'dog'
    V -> 'chased'|'saw'
""")
parser=nltk.ChartParser(grammar)
sentence="the dog chased the cat".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
