from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from gensim.utils import simple_preprocess

def train_doc2vec_model(tagged_train_data):
    print("hey i am inside train_doc2vec_model")
    model = Doc2Vec(vector_size=100, window=5, min_count=1, workers=4, epochs=10)
    model.build_vocab(tagged_train_data)
    model.train(tagged_train_data, total_examples=model.corpus_count, epochs=model.epochs)
    return model
