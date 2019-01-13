#! python3

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for each in doc.paragraphs:
        fullText.append(each.text)
    return "\n".join(fullText)