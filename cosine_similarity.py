from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity_score(sentence1, sentence2):
    vectorizer = CountVectorizer().fit_transform([sentence1, sentence2])
    vectors = vectorizer.toarray()
    similarity = cosine_similarity(vectors)
    return similarity[0][1]

sentence1 = "Chunking aids in memorizing vocabulary by grouping related words together."
sentence2 = "Grouping related words together helps in memorizing vocabulary with chunking."

# Calculate cosine similarity
similarity_score = cosine_similarity_score(sentence1, sentence2)
print(f"Cosine similarity between the two sentences: {similarity_score}")
