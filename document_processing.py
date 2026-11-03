import re

def search_document(text, keyword):
    lines = text.splitlines()
    matches = []
    for line in lines:
        if keyword.lower() in line.lower():
            matches.append(line)
    return matches

def split_text(text):
    if not text or not text.strip():
        return []

    # Split sentences while protecting decimals and common abbreviations
    pattern = (
        r"(?<!\bInc\.)(?<!\bCorp\.)(?<!\bCo\.)"
        r"(?<!\bLtd\.)(?<!\bDr\.)(?<!\bMr\.)"
        r"(?<=[.!?])\s+"
    )

    sentences = re.split(pattern, text.strip(), flags=re.IGNORECASE)
    
    cleaned_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
       
        if sentence:
            cleaned_sentences.append(sentence)
   
    return cleaned_sentences


def sentence_extract(text, max_sentences):
    if max_sentences <= 0:
        return ""

    sentences = split_text(text)

    return " ".join(sentences[:max_sentences])