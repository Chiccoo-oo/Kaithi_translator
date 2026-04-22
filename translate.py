import torch
import torch.nn as nn
import pandas as pd

# SAME model as training
class Model(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, 128)
        self.lstm = nn.LSTM(128, 128, batch_first=True)
        self.fc = nn.Linear(128, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        x, _ = self.lstm(x)
        return self.fc(x)


# Load dataset to rebuild vocab

import json

with open("vocab.json", "r", encoding="utf-8") as f:
    char2idx = json.load(f)

# convert keys properly
idx2char = {int(v): k for k, v in char2idx.items()}
vocab_size = len(char2idx)
# SAFE encode (no crash)
def encode(text):
    return [char2idx.get(c, 0) for c in text]


def decode(indices):
    text = "".join([idx2char[i] for i in indices])
    
    # Remove special tokens
    text = text.replace("<s>", "").replace("</s>", "")
    
    return text.strip()


# Load model
model = Model(vocab_size)
model.load_state_dict(torch.load("model.pth"))
model.eval()


def translate(text):
    # add tokens (VERY IMPORTANT)
    text = "<s>" + text + "</s>"

    x = torch.tensor([encode(text)])
    output = model(x)

    pred = output.argmax(dim=2)[0].tolist()
    return decode(pred)


# Loop
while True:
    kaithi_input = input("Enter Kaithi: ")
    print("Hindi:", translate(kaithi_input))