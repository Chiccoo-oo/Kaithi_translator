# make_small_corpus.py

base = [
    "भारत एक महान देश है",
    "मेरा नाम अनुष्का है",
    "तुम कैसे हो",
    "आज मौसम अच्छा है",
    "मुझे मशीन लर्निंग पसंद है"
]

with open("hindi_corpus.txt", "w", encoding="utf-8") as f:
    for i in range(100):  # 100 × 5 = 500 sentences
        for sentence in base:
            f.write(sentence + "\n")