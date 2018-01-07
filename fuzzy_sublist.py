from Levenshtein import ratio


test = [
        'abc',
        'gh',
        'def'
        ]

def build(i, list_, sentences, candidate):
    if i == len(list_):
        sentences.append(candidate)
    else:
        for elem in list_[i]:
            build(i+1, list_, sentences, candidate + [elem])

sentences = []
build(0, test, sentences, [])
print(sentences)
