from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

documents = [
    "The quick brown fox jumps over the lazy dog",
    "A brown dog chased the fox",
    "The fox is quick and the dog is lazy",
    "The cat is sitting on the windowsill",
]

query = "The quick fox"

def tfidf_search(query, documents):
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents + [query])

    cosine_similarities = linear_kernel(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

    ranked_documents = sorted(enumerate(cosine_similarities), key=lambda x: x[1], reverse=True)

    return ranked_documents

results = tfidf_search(query, documents)

print("Ranked Documents:")
for index, similarity in results:
    print(f"Document {index + 1}: Similarity = {similarity:.4f}")
    print(f"   '{documents[index]}'\n")
