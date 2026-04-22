import pandas as pd
from converter import hindi_to_kaithi

# Load Hindi sentences from file
def load_sentences(file_path):
    sentences = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:  # skip empty lines
                    sentences.append(line)
    except FileNotFoundError:
        print("hindi_corpus.txt not found! Using sample sentences.")
        sentences = [
            "मेरा नाम अनुष्का है",
            "तुम कैसे हो",
            "यह एक परीक्षण है",
            "भारत एक महान देश है",
            "मुझे मशीन लर्निंग पसंद है"
        ]
    return sentences


def generate_dataset(input_file="hindi_corpus.txt", output_file="dataset.csv"):
    hindi_sentences = load_sentences(input_file)

    data = []

    for sentence in hindi_sentences:
        try:
            kaithi = hindi_to_kaithi(sentence)
            data.append([kaithi, sentence])
        except Exception as e:
            print(f"Error processing: {sentence}")
            continue

    df = pd.DataFrame(data, columns=["kaithi", "hindi"])

    # Remove duplicates (important for ML)
    #df = df.drop_duplicates()

    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"Dataset created with {len(df)} samples!")


if __name__ == "__main__":
    generate_dataset()