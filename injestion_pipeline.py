import numpy as np
# import 



def chunk_by_char(text, size=200, overlap=199):
    if overlap >= size:
        raise ValueError("Overlap must be smaller that chunk size")
    step = size-overlap
    chunks=[]
    for i in range(0, len(text), step):
        pieces = text[i:i + size].strip()
        if pieces:
            chunks.append(pieces)
    return chunks

text = open("sample.txt", encoding="utf-8").read()

cunks = chunk_by_char(text, overlap=50)

for i, c in enumerate(cunks[:3]):
    print(f"--- chunk {i} ---")
    print(c)
    
    