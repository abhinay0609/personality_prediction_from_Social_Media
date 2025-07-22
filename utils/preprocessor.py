import string
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    text = ''.join([char for char in text if char not in string.punctuation])
    return text
