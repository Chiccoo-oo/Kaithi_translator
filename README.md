# Kaithi-Hindi Translator

A specialized tool for transliterating and translating between the historical **Kaithi** script and modern **Hindi** (Devanagari). This project combines rule-based mapping with deep learning to provide accurate script conversion.

## 🌟 Overview

Kaithi is a historical script used widely in North India for legal, administrative, and religious records. This project aims to bridge the gap between historical Kaithi documents and modern Hindi.

- **Hindi → Kaithi**: Rule-based mapping using Unicode character sets.
- **Kaithi → Hindi**: Neural-network based translation using a Character-level LSTM (Long Short-Term Memory) model to handle script nuances.

## 📂 Project Structure

- `converter.py`: Core logic for rule-based Hindi-to-Kaithi transliteration.
- `translate.py`: Interactive inference script to translate Kaithi text back to Hindi using the trained model.
- `train_model.py`: Training pipeline for the LSTM sequence model.
- `generate_data.py`: Utility to create training datasets (`dataset.csv`) from Hindi corpora.
- `vocab.json`: Character vocabulary used by the neural network.
- `model.pth`: Pre-trained PyTorch model weights.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- PyTorch
- Pandas

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chiccoo-oo/Kaithi_translator.git
   cd Kaithi_translator
   ```

2. Install dependencies:
   ```bash
   pip install torch pandas
   ```

### Usage

#### 1. Translation (Kaithi to Hindi)
Run the interactive translation script:
```bash
python translate.py
```

#### 2. Data Generation
If you want to expand the dataset using a new Hindi corpus (`hindi_corpus.txt`):
```bash
python generate_data.py
```

#### 3. Training
To retrain the model on your dataset:
```bash
python train_model.py
```

## 🧠 Model Architecture

The translation model uses a Character-level Sequence Model:
- **Embedding Layer**: Converts characters to 128-dimensional vectors.
- **LSTM Layer**: Captures sequential context within the script.
- **Linear Layer**: Maps hidden states back to the character vocabulary.

## 📝 License

This project is open-source and available for educational and research purposes.
