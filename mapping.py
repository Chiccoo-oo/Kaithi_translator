from datasets import load_dataset
import pandas as pd
from converter import hindi_to_kaithi

# Load dataset
ds = load_dataset("cfilt/iitb-english-hindi")

data = []

# Use train split (you can also use validation/test)
for example in ds["train"]:
    hindi = example["translation"]["hi"].strip()

    if not hindi:
        continue

    try:
        kaithi = hindi_to_kaithi(hindi)
        data.append([kaithi, hindi])
    except Exception as e:
        # Skip problematic lines
        continue

# Convert to DataFrame
df = pd.DataFrame(data, columns=["kaithi", "hindi"])

# Save dataset
df.to_csv("dataset.csv", index=False, encoding="utf-8")

print("Dataset created from IITB!")