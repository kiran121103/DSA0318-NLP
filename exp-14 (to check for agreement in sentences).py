import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> 'he' | 'she' | 'dog'
    NP_PL -> 'they' | 'cats'
    VP_SG -> V_SG | V_SG NP_SG
    VP_PL -> V_PL | V_PL NP_PL
    V_SG -> 'runs' | 'eats'
    V_PL -> 'run' | 'eat'
""")

parser = nltk.ChartParser(grammar)

sentence = "he runs"

tokens = sentence.split()

agreement = False
for tree in parser.parse(tokens):
    agreement = True

if agreement:
    print("The sentence follows the subject-verb agreement rules.")
else:
    print("The sentence does not follow the subject-verb agreement rules.")
