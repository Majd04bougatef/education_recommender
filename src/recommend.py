import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Importer les données prétraitées depuis preprocessing.py
from src.preprocessing import df  # Assure-toi que df est bien exporté dans preprocessing.py

# Vectorisation TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df["combined_features"])

# Calcul de la similarité cosinus
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index des titres
indices = pd.Series(df.index, index=df["title"])

# Fonction de recommandation
def get_recommendations(title, n=3):
    if title not in indices:
        return f" Titre « {title} » non trouvé dans le dataset."

    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]
    resource_indices = [i[0] for i in sim_scores]
    return df.iloc[resource_indices][["title", "topic", "format", "difficulty"]]

# Test
if __name__ == "__main__":
    test_title = "Intro to Python"
    print(f"\n Recommandations pour : {test_title}")
    print(get_recommendations(test_title))
