document_text = """
Amazon reported net sales of $180 billion.
Operating income increased compared to last year.
Revenue growth was driven by AWS.
Net income increased during the quarter.
"""

search_term = "income"

def search_document(text, keyword):
    lines = text.splitlines()
    matches = []
    for line in lines:
        if keyword.lower() in line.lower():
            matches.append(line)
    return matches

results = search_document(document_text, "profit")
print(results)