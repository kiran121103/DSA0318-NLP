import re
text = "The quick brown fox jumps over the lazy dog"
patterns = [
    (r'\bthe\b', 'DET'),       
    (r'\bquick\b', 'ADJ'),     
    (r'\bbrown\b', 'ADJ'),
    (r'\bfox\b', 'NOUN'),      
    (r'\bjumps\b', 'VERB'),    
    (r'\bover\b', 'PREP'),     
    (r'\blazy\b', 'ADJ'),
    (r'\bdog\b', 'NOUN')
]
tokens = text.split()
def pos_tag(tokens, patterns):
    tagged_tokens = []
    for token in tokens:
        tag = 'UNK'  
        for pattern, pos in patterns:
            if re.fullmatch(pattern, token, re.IGNORECASE):
                tag = pos
                break
        tagged_tokens.append((token, tag))
    return tagged_tokens
tagged_tokens = pos_tag(tokens, patterns)
for token, tag in tagged_tokens:
    print(f"{token}: {tag}")
