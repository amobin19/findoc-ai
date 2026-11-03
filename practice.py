import re

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

text_day4 = "Amazon reported growth. AWS revenue increased. Operating income improved."

def split_text(text):
    split_up = text.split(".")
    split_list = []
    for i in split_up:
        i = i.strip()
        if i:
            split_list.append(i)
    return split_list

results_day4 = split_text(text_day4)

# for line in results_day4:
#     print(line)

def summarize_document(text,max_sentences):
    split_list = split_text(text)
    new_list = []
    for i in split_list[:max_sentences]:
        new_list.append(i)
    if len(new_list) == 0:
        return ""
    return ". ".join(new_list)+"."

text_day4_2 = "Amazon earned $200 million. AWS earned $50 million. Profit was $27 million."
numbers = re.findall(r"\d+",text_day4_2)

text_day4_3 = "Amazon revenue was $200.6 billion. Operating income reached $27.5 billion. AWS grew 37%."

# Split at whitespace that follows a period
# (?<=\.) checks for a period before the space without removing it; \s+ matches one or more spaces
sentences = re.split(r"(?<=\.)\s+", text_day4_3.strip())
print (sentences)
