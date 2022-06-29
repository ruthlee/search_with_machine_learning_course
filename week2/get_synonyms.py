import pandas as pd
import fasttext

model = fasttext.load_model("../../../workspace/datasets/fasttext/title_model.bin")

with open('../../../workspace/datasets/fasttext/top_words.txt') as t:
    words = t.read().splitlines()

result = []

for word in words:
    sims = []
    sims.append(word)
    nns = model.get_nearest_neighbors(word)
    for nn in nns:
        if nn[0] > 0.8:
            sims.append(nn[1])
    result.append(",".join(sims))

print(result)

with open('../../../workspace/datasets/fasttext/synonyms.csv', mode='wt') as myfile:
    myfile.write('\n'.join(result))

print("written to: ../../../workspace/datasets/fasttext/synonyms.csv")
