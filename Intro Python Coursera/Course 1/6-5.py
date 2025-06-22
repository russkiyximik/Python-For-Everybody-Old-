text = "X-DSPAM-Confidence:    0.8475"
stripped = text[text.find(" "):]
stripped = float(stripped.strip())
print(stripped)