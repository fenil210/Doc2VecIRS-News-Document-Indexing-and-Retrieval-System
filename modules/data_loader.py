import os
import pandas as pd
from gensim.parsing.preprocessing import preprocess_string, strip_tags, strip_numeric, strip_punctuation, strip_multiple_whitespaces

def load_data(data_dir):
    print("hey i am inside load_data")
    data = []
    target = []
    for category in os.listdir(data_dir):
        cat_path = os.path.join(data_dir, category)
        if os.path.isdir(cat_path):
            for document in os.listdir(cat_path):
                doc_path = os.path.join(cat_path, document)
                with open(doc_path, "r", errors="ignore") as f:
                    data.append(f.read())
                    target.append(category)
    return pd.DataFrame({'text': data, 'target': target})

def preprocess_text(text):
    print("hey i am inside preprocess_text")

    filters = [
        lambda x: x.lower(),
        strip_tags,
        strip_numeric,
        strip_punctuation,
        strip_multiple_whitespaces
    ]
    return ' '.join(preprocess_string(text, filters=filters))
