def search_document(text, keyword):
    lines = text.splitlines()
    matches = []
    for line in lines:
        if keyword.lower() in line.lower():
            matches.append(line)
    return matches