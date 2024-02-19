import os
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
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
    text = text.lower()
    text = re.sub(r'<.*?>', '', text)

#     text = re.sub(r'\d+', '', text)

    text = re.sub(r'[^\w\s]', '', text)

    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word not in stop_words]

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

    return ' '.join(lemmatized_words)
