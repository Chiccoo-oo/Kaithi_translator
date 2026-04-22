import random

subjects = ["मैं", "तुम", "वह", "हम", "राम", "सीता"]
verbs = ["खा रहा हूँ", "जा रहा हूँ", "पढ़ रहा हूँ", "लिख रहा हूँ", "देख रहा हूँ"]
objects = ["किताब", "खाना", "स्कूल", "घर", "बाजार"]
extras = ["आज", "कल", "अभी", "जल्दी", "धीरे"]

sentences = []

for _ in range(1000):  # generate 1000 sentences
    s = random.choice(subjects)
    v = random.choice(verbs)
    o = random.choice(objects)
    e = random.choice(extras)

    sentence = f"{e} {s} {o} {v}"
    sentences.append(sentence)

# save
with open("hindi_corpus.txt", "w", encoding="utf-8") as f:
    for s in sentences:
        f.write(s + "\n")

print("Better corpus generated!")