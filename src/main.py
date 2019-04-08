from janome.tokenizer import Tokenizer
import pandas as pd
df = pd.read_json('./momota-sd.jsonl', orient='records', lines=True, encoding='utf-8')
t = Tokenizer(udic="./momoclo-dict.csv", udic_enc="utf8")

for i, row in df.head(10).iterrows():
  text = row['text']
  wakati = t.tokenize(text, wakati=True)
  print(wakati)
