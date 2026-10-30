import numpy as np
import re



def chunk_by_char(text, size=200, overlap=100):
    if overlap >= size:
        raise ValueError("Overlap must be smaller that chunk size")
    step = size-overlap
    chunks=[]
    for i in range(0, len(text), step):
        pieces = text[i:i + size].strip()
        if pieces:
            chunks.append(pieces)
    return chunks

def tokenize(text) :
    # return text.lower().split()
    return re.findall(r"[a-z0-9]+", text.lower())


def score(question, chunk):
    q_word = set(tokenize(question))
    c_word = set(tokenize(chunk))
    return len(q_word & c_word)


def search(question, chunk):
    scored = []
    for i, c in enumerate(chunk):
        scored.append((score(question, c), i))
    scored.sort(reverse=True)
    
    return scored[:3]
    
text = open("sample.txt", encoding="utf-8").read()

question = "When was hello first used"
cunks = chunk_by_char(text, overlap=50)

results = search(question, cunks)

for s, i in results:
    print(f"--- Chunk {i} --- score {s} ---")
    print(cunks[i])
# for i, c in enumerate(cunks[:3]):
#     print(f"--- chunk {i} ---")
#     print(search[])
    
# print(tokenize("Hello, with that spelling, was used"))