from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import pickle
import sqlite3
import os
import sys
sys.path.append('../ml_models')
sys.path.append('.')
from train_models import recommend_tfidf, recommend_word2vec, get_recipe_vector_word2vec
from database import create_database, get_recipes_from_db

app = Flask(__name__)
CORS(app)

# Load models and data
tfidf_vectorizer = None
tfidf_matrix = None
word2vec_model = None
recipes_df = None

def load_models():
    global tfidf_vectorizer, tfidf_matrix, word2vec_model, recipes_df
    try:
        with open('../ml_models/tfidf_vectorizer.pkl', 'rb') as f:
            tfidf_vectorizer = pickle.load(f)
        with open('../ml_models/tfidf_matrix.pkl', 'rb') as f:
            tfidf_matrix = pickle.load(f)
        word2vec_model = Word2Vec.load('../ml_models/word2vec.model')
        recipes_df = pd.read_csv('../data/sample_recipes.csv')
        recipes_df['ingredients'] = recipes_df['ingredients'].str.split(',')
        print("Models loaded successfully")
    except FileNotFoundError:
        print("Models not found. Please train models first.")

@app.route('/recommend', methods=['POST'])
def recommend_recipes():
    data = request.get_json()
    print("Backend: Received request data:", data)
    ingredients = [ing.lower().strip() for ing in data.get('ingredients', [])]
    region = data.get('region', None)
    diet = data.get('diet', None)
    print("Backend: Processed ingredients:", ingredients, "region:", region, "diet:", diet)

    if tfidf_vectorizer is None or recipes_df is None:
        print("Backend: Models not loaded")
        return jsonify({'error': 'Models not loaded'}), 500

    # Filter recipes based on region and diet
    filtered_df = recipes_df.copy()
    if region and region.strip():
        filtered_df = filtered_df[filtered_df['region'] == region]
    if diet and diet.strip():
        filtered_df = filtered_df[filtered_df['diet'] == diet]
    print("Backend: Filtered recipes count:", len(filtered_df))

    if filtered_df.empty:
        print("Backend: No recipes match filters")
        return jsonify({'recommendations': []})

    # Get recommendations using TF-IDF
    try:
        recommended_recipes = recommend_tfidf(ingredients, tfidf_vectorizer, tfidf_matrix, filtered_df, top_n=5)
        print("Backend: TF-IDF recommendations found:", len(recommended_recipes))
    except Exception as e:
        print("Backend: TF-IDF failed, falling back to Word2Vec:", str(e))
        # Fallback to Word2Vec if TF-IDF fails
        recommended_recipes = recommend_word2vec(ingredients, word2vec_model, filtered_df, top_n=5)
        print("Backend: Word2Vec recommendations found:", len(recommended_recipes))

    recommendations = []
    for _, recipe in recommended_recipes.iterrows():
        rec = {
            'name': recipe['name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe.get('instructions', 'No instructions available'),
            'region': recipe['region'],
            'diet': recipe['diet']
        }
        recommendations.append(rec)
    print("Backend: Returning recommendations:", len(recommendations))

    return jsonify({'recommendations': recommendations})

@app.route('/recipes', methods=['GET'])
def get_recipes():
    if recipes_df is None:
        return jsonify({'error': 'Data not loaded'}), 500

    recipes = []
    for _, recipe in recipes_df.iterrows():
        recipes.append({
            'name': recipe['name'],
            'ingredients': recipe['ingredients'],
            'instructions': recipe.get('instructions', 'No instructions available'),
            'region': recipe['region'],
            'diet': recipe['diet']
        })

    return jsonify({'recipes': recipes})

if __name__ == '__main__':
    load_models()
    app.run(debug=True)
