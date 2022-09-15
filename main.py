from pdfminer.high_level import extract_text
text = extract_text('documents/iitm2022engineering.pdf')
print(repr(text))
print(text)