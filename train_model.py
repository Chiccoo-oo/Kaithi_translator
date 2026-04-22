import torch
import torch.nn as nn
import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

kaithi_texts = df["kaithi"].tolist()
hindi_texts = df["hindi"].tolist()

# Character-level vocab
all_text = "".join(kaithi_texts + hindi_texts)
chars = sorted(list(set(all_text)))   # FIXED ORDER

char2idx = {c:i for i,c in enumerate(chars)}
idx2char = {i:c for c,i in char2idx.items()}

# SAVE vocab
import json
with open("vocab.json", "w", encoding="utf-8") as f:
    json.dump(char2idx, f, ensure_ascii=False)

vocab_size = len(chars)

def encode(text):
    return [char2idx[c] for c in text]

def decode(indices):
    return "".join([idx2char[i] for i in indices])
class Seq2Seq(nn.Module):
    def __init__(self, vocab_size, hidden_size=128):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.lstm(x)
        out = self.fc(out)
        return out

model = Seq2Seq(vocab_size)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
epochs = 20

for epoch in range(epochs):
    total_loss = 0

    for k, h in zip(kaithi_texts, hindi_texts):
        x = torch.tensor([encode(k)])
        y = torch.tensor([encode(h)])

        output = model(x)

        loss = criterion(output.view(-1, vocab_size), y.view(-1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch+1}, Loss: {total_loss}")
    torch.save(model.state_dict(), "model.pth")