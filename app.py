from flask import Flask, render_template, request, redirect, url_for
from modules.data_loader import load_data, preprocess_text
from modules.doc2vec_trainer import train_doc2vec_model
from modules.query_handler import retrieve_top_k_documents, evaluate_precision_recall
import os
import pandas as pd
from gensim.models.doc2vec import TaggedDocument
from gensim.utils import simple_preprocess
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

data_dir = "C:/Users/Fenil/OneDrive/Desktop/Sem 6/IRS/LAB 4/20news-bydate-test"
df = load_data(data_dir)
df['text'] = df['text'].apply(preprocess_text)

tagged_train_data = [TaggedDocument(simple_preprocess(text), [i]) for i, text in enumerate(df['text'])]
model = train_doc2vec_model(tagged_train_data)
inferred_vectors = [model.infer_vector(simple_preprocess(text)) for text in df['text']]

@app.route('/')
def index():
    return render_template('index.html', df=df)

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    query_target = request.form['query_target']
    k = int(request.form['k'])
    query = preprocess_text(query)
    query_vector = model.infer_vector(simple_preprocess(query))
    ranked_indices, similarity_scores = retrieve_top_k_documents(query_vector, inferred_vectors, k)
    precision, recall = evaluate_precision_recall(ranked_indices, df, query_target, k)

    # Convert numpy arrays to Python lists
    ranked_indices = ranked_indices.tolist()
    similarity_scores = similarity_scores.tolist()

    return render_template('index.html', ranked_indices=ranked_indices, similarity_scores=similarity_scores, precision=precision, recall=recall, df=df)

@app.route('/view_document/<int:document_index>')
def view_document(document_index):
    document_content = df.iloc[document_index]['text']
    return render_template('view_document.html', document_content=document_content)


if __name__ == '__main__':
    app.run(debug=True)

# pip install virtualenv
    # virtualenv --version
# python -m venv virtual 
    # . virtual/bin/activate

# pip install Flask gensim pandas numpy scikit-learn numpy 
# python app.py
    
# python -m flask --app .\app.py run
   