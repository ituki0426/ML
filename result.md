# 1.学習用データ

## (1)イヤホン1
![イヤホン1](https://github.com/ituki0426/AI/assets/82156802/8d8a5016-5f25-464f-8a9d-a448c7835ad1)

{"description": "black wireless earbud"}


## (2)イヤホン2
![イヤホン2](https://github.com/ituki0426/AI/assets/82156802/bacfc66b-3a09-4a1e-a400-4ba4101fa2fd)

{“description":"A white pair of wireless earbuds in a charging case, with the case partially enclosed in a small black leather pouch with a snap button closure. The case has a text that reads 'shuichi' on it."}



## (3)イヤホン3
![イヤホン3](https://github.com/ituki0426/AI/assets/82156802/17dfbdef-681e-4bed-b4ab-40c096136be4)

{"description": "a pair of white wireless earbuds with a charging case"}

## (4)イヤホン4

![イヤホン4](https://github.com/ituki0426/AI/assets/82156802/06df3158-ea52-49f9-b2a7-2ac72761daad)

{"description": "A pair of white wired earphones with an in-line remote and a Lightning connector for Apple devices"}

## (5)イヤホン5
![イヤホン5](https://github.com/ituki0426/AI/assets/82156802/9636b0b2-7300-40ee-9280-f319220fc1ff)

{"description": "A pair of wireless earbuds with a black charging case. The case has a distinctive 'b' logo on the top and is open to reveal one earbud inside. The earbuds appear to be black with a small red marking indicating the right side earbud is missing from the case."}

## (4)スマホ1

![スマホ1](https://github.com/ituki0426/AI/assets/82156802/264a9fd6-9a34-48eb-a4f5-cbe0f03ca973)

{"description":"A smartphone with a floral pattern case, featuring yellow and red flowers with green leaves on a cream background. The case is slightly worn at the edges and encapsulates the phone's rear cameras."}

## (5)スマホ2
![スマホ2](https://github.com/ituki0426/AI/assets/82156802/a296aa15-788b-4e03-9dac-8dde43d35b27)
The 
{"description":"clear smartphone case with a graphic of a lobster"}

## (6)スマホ3
![スマホ3](https://github.com/ituki0426/AI/assets/82156802/18d5fc97-db1a-40fb-a8d9-6ea0e756ca0d)

{"description":"brown leather smartphone wallet case with a closure strap"}

## (7)鍵1
![鍵1](https://github.com/ituki0426/AI/assets/82156802/f804af78-fe77-46a6-a7c7-54da6ad25833)

{"description": "A set of keys held in a person's hand"}

## (8)鍵2
![鍵２](https://github.com/ituki0426/AI/assets/82156802/e5c3778f-e610-4d61-8995-acb74c25295c)
{"description": "A small metal padlock with a silver finish and horizontal ridges on the body, attached to a black key with a plastic key cover and black cord looped through the key cover."}

## (9)鍵3
![鍵3](https://github.com/ituki0426/AI/assets/82156802/96e04492-03c6-428a-84b1-4a6d29f103b0)

{"description": "A set of keys with a distinctive yellow keychain labeled 'XLARGE'"}

## (10)財布1
![財布1](https://github.com/ituki0426/AI/assets/82156802/8f200427-1b80-462e-b2c2-ef3d1af0d997)
The 
{"description": "A black leather wallet with a zipper closure"}

## (11)財布2
![財布2](https://github.com/ituki0426/AI/assets/82156802/51ec409e-752b-47c4-846c-28633f62724c)

{"description": "A patterned, bifold wallet with a brown and tan circular design and a dark brown leather trim and clasp."}

## (14)財布3

![財布3](https://github.com/ituki0426/AI/assets/82156802/e83c62d0-48b2-4efe-abec-e22b3da1f552)


# 2.比較用データ

## (1)BERT

Query: That is a happy person

Rank: Title Similarity

1: That is a very happy person 0.9840199310313991

2: That is a happy dog 0.9668645682039443

3: Today is a sunny day 0.8785718352937959

---

Query: A red iPhone 15 with a broken screen

Rank: Title Similarity

1: A cracked red iPhone 15 0.9082752924314121

2: A brown wallet that has damage 0.9056091995924238

3: The new blue iPhone 0.7978265169338986

## (2)all-Mini-LM-L12-v2

Query: That is a happy person

Rank: Title Similarity

1: That is a very happy person 0.9205622673034668

2: That is a happy dog 0.748626172542572

3: Today is a sunny day 0.23271775245666504

---

Query: A red iPhone 15 with a broken screen

Rank: Title Similarity

1: A cracked red iPhone 15 0.8165010809898376

2: The new blue iPhone 0.42757079005241394

3: A brown wallet that has damage 0.2572976052761078

## (3)OpenAI
Query: That is a happy person

Rank: Title Similarity

1: That is a very happy person 0.9834585470466383

2: That is a happy dog 0.9300421542369247

3: Today is a sunny day 0.8225563953706708

---

Query: A red iPhone 15 with a broken screen

Rank: Title Similarity

1: A cracked red iPhone 15 0.9576859933904734

2: The new blue iPhone 0.8781633863308884

3: A brown wallet that has damage 0.8251047274310378