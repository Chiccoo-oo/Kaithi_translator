const inputText = document.getElementById('input-text');
const outputText = document.getElementById('output-text');
const translateBtn = document.getElementById('translate-btn');
const btnK2H = document.getElementById('btn-k2h');
const btnH2K = document.getElementById('btn-h2k');
const inputLabel = document.getElementById('input-label');
const outputLabel = document.getElementById('output-label');
const copyBtn = document.getElementById('copy-btn');

let mode = 'k2h'; // k2h or h2k

// Toggle Modes
btnK2H.addEventListener('click', () => {
    mode = 'k2h';
    btnK2H.classList.add('active');
    btnH2K.classList.remove('active');
    inputLabel.innerText = 'Kaithi Script';
    outputLabel.innerText = 'Hindi (Devanagari)';
    inputText.placeholder = 'Paste Kaithi script here...';
    outputText.innerText = 'Translation will appear here...';
    outputText.style.fontFamily = "'Noto Sans Devanagari', sans-serif";
});

btnH2K.addEventListener('click', () => {
    mode = 'h2k';
    btnH2K.classList.add('active');
    btnK2H.classList.remove('active');
    inputLabel.innerText = 'Hindi (Devanagari)';
    outputLabel.innerText = 'Kaithi Script';
    inputText.placeholder = 'Type Hindi here...';
    outputText.innerText = 'Transliteration will appear here...';
    // Kaithi often needs special font support, but we'll use default or system fonts for now
    outputText.style.fontFamily = "'Inter', sans-serif";
});

// Translation Logic
async function handleTranslation() {
    const text = inputText.value.trim();
    if (!text) return;

    translateBtn.innerText = 'Translating...';
    translateBtn.disabled = true;

    const endpoint = mode === 'k2h' ? '/api/kaithi-to-hindi' : '/api/hindi-to-kaithi';

    try {
        const response = await fetch(endpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });

        if (!response.ok) throw new Error('Translation failed');

        const data = await response.json();
        outputText.innerText = data.translated;
    } catch (error) {
        console.error(error);
        outputText.innerText = 'Error: Could not translate. Make sure the server is running.';
        outputText.style.color = '#ef4444';
    } finally {
        translateBtn.innerText = 'Translate';
        translateBtn.disabled = false;
    }
}

translateBtn.addEventListener('click', handleTranslation);

// Copy to Clipboard
copyBtn.addEventListener('click', () => {
    const text = outputText.innerText;
    if (text && !text.includes('will appear here')) {
        navigator.clipboard.writeText(text).then(() => {
            const originalSvg = copyBtn.innerHTML;
            copyBtn.innerHTML = '<svg viewBox="0 0 24 24" width="18" height="18"><path fill="#10b981" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>';
            setTimeout(() => copyBtn.innerHTML = originalSvg, 2000);
        });
    }
});

// Optional: Translate on Enter (Cmd/Ctrl + Enter)
inputText.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        handleTranslation();
    }
});
