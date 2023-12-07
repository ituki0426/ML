import openai
import numpy as np
import json
from transformers import BertJapaneseTokenizer
from transformers import BertModel

tokenizer = BertJapaneseTokenizer.from_pretrained(
    'cl-tohoku/bert-base-japanese-whole-word-masking')
bert_model = BertModel.from_pretrained(
    'cl-tohoku/bert-base-japanese-whole-word-masking')


# データベースの読み込み
with open('./index.json') as f:
    INDEX = json.load(f)

# これが検索用の文字列
QUERY = "A red iPhone 15 with a broken screen"

# 検索用の文字列をベクトル化

input_f = tokenizer(QUERY, return_tensors="pt")
outputs = bert_model(**input_f)
last_hidden_states = outputs.last_hidden_state

attention_mask = input_f.attention_mask.unsqueeze(-1)
valid_token_num = attention_mask.sum(1)
sentence_vec = (last_hidden_states*attention_mask).sum(1) / valid_token_num
query = sentence_vec.detach().cpu().numpy()[0]


# 総当りで類似度を計算
results = map(
    lambda i: {
        'title': i['title'],
        # ここでクエリと各文章のコサイン類似度を計算
        'similarity': np.dot(np.array(i['embedding']), query) / (np.linalg.norm(np.array(i['embedding'])) * np.linalg.norm(query))
    },
    INDEX
)
# コサイン類似度で降順（大きい順）にソート
results = sorted(results, key=lambda i: i['similarity'], reverse=True)

# 以下で結果を表示
print(f"Query: {QUERY}")
print("Rank: Title Similarity")
for i, result in enumerate(results):
    print(f'{i+1}: {result["title"]} {result["similarity"]}')
