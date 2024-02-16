import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def retrieve_top_k_documents(query_vector, inferred_vectors, k):
    print("hey i am inside retrieve_top_k_documents")

    similarity_scores = cosine_similarity(query_vector.reshape(1, -1), inferred_vectors).flatten()
    ranked_indices = np.argsort(similarity_scores)[::-1][:k]
    return ranked_indices, similarity_scores[ranked_indices]

def evaluate_precision_recall(ranked_indices, df ,query_target,k):
    relevant_documents = 0
    retrieved_relevant_documents = 0
    for i in range(k):
        if df.iloc[ranked_indices[i]]['target'] == query_target:
            retrieved_relevant_documents += 1
            if i < len(df[df['target'] == query_target]):
                relevant_documents += 1
    precision = retrieved_relevant_documents / k
    recall = relevant_documents / len(df[df['target'] == query_target])
    return precision, recall


