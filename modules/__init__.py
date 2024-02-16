# modules/__init__.py

from .data_loader import load_data, preprocess_text
from .doc2vec_trainer import train_doc2vec_model
from .query_handler import retrieve_top_k_documents, evaluate_precision_recall