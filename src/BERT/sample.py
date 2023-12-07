from transformers import BertJapaneseTokenizer
from transformers import BertModel
import torch
import pandas as pd
import numpy as np

tokenizer = BertJapaneseTokenizer.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
bert_model = BertModel.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')

print("text1")
text_1 = input()

input_s = tokenizer(text_1, return_tensors="pt")

outputs = bert_model(**input_s)
last_hidden_states = outputs.last_hidden_state

attention_mask = input_s.attention_mask.unsqueeze(-1)
valid_token_num = attention_mask.sum(1)

base_vec = (last_hidden_states*attention_mask).sum(1) / valid_token_num
base_vec = base_vec.detach().cpu().numpy()[0]

print("text2")
text_2 = input()

input_f = tokenizer(text_2, return_tensors="pt")
outputs = bert_model(**input_f)
last_hidden_states = outputs.last_hidden_state

attention_mask = input_f.attention_mask.unsqueeze(-1)
valid_token_num = attention_mask.sum(1)
sentence_vec = (last_hidden_states*attention_mask).sum(1) / valid_token_num
sentence_vec = sentence_vec.detach().cpu().numpy()[0]
cos = np.dot(base_vec, sentence_vec) / (np.linalg.norm(base_vec) * np.linalg.norm(sentence_vec))

print(cos)
