import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import pickle
import os

def train_tfidf_model(recipes_df):
    # Create ingredient_text if not present
    if 'ingredient_text' not in recipes_df.columns:
        recipes_df['ingredient_text'] = recipes_df['ingredients'].apply(lambda x: ' '.join(x))

    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(recipes_df['ingredient_text'])

    # Save model
    with open('tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    with open('tfidf_matrix.pkl', 'wb') as f:
        pickle.dump(tfidf_matrix, f)

    return vectorizer, tfidf_matrix

def train_word2vec_model(recipes_df):
    # Prepare sentences for Word2Vec
    sentences = recipes_df['ingredients'].tolist()

    model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
    model.save('word2vec.model')

    return model

def get_recipe_vector_word2vec(ingredients, model):
    vectors = []
    for ingredient in ingredients:
        if ingredient in model.wv:
            vectors.append(model.wv[ingredient])
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

def recommend_tfidf(user_ingredients, vectorizer, tfidf_matrix, recipes_df, top_n=5):
    user_text = ' '.join(user_ingredients)
    user_vector = vectorizer.transform([user_text])
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return recipes_df.iloc[top_indices]

def recommend_word2vec(user_ingredients, model, recipes_df, top_n=5):
    user_vector = get_recipe_vector_word2vec(user_ingredients, model)
    similarities = []

    for _, row in recipes_df.iterrows():
        recipe_vector = get_recipe_vector_word2vec(row['ingredients'], model)
        sim = cosine_similarity([user_vector], [recipe_vector])[0][0]
        similarities.append(sim)

    similarities = np.array(similarities)
    top_indices = similarities.argsort()[-top_n:][::-1]
    return recipes_df.iloc[top_indices]

if __name__ == '__main__':
    if os.path.exists('../data/sample_recipes.csv'):
        recipes_df = pd.read_csv('../data/sample_recipes.csv')
        recipes_df['ingredients'] = recipes_df['ingredients'].apply(eval)  # Convert string back to list

        print("Training TF-IDF model...")
        tfidf_vectorizer, tfidf_matrix = train_tfidf_model(recipes_df)

        print("Training Word2Vec model...")
        word2vec_model = train_word2vec_model(recipes_df)

        print("Models trained and saved.")
    else:
        print("Processed data not found. Run preprocess.py first.")
