import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

def load_datasets():
    # Check for actual datasets first, fallback to sample data
    recipes_path = 'indian_food.csv'
    sample_path = 'sample_recipes.csv'

    if os.path.exists(recipes_path):
        recipes_df = pd.read_csv(recipes_path)
        ingredients_df = recipes_df[['name', 'ingredients']].copy()
        ingredients_df['ingredients'] = ingredients_df['ingredients'].str.split(',')
    elif os.path.exists(sample_path):
        recipes_df = pd.read_csv(sample_path)
        ingredients_df = recipes_df[['name', 'ingredients']].copy()
        ingredients_df['ingredients'] = ingredients_df['ingredients'].str.split(',')
    else:
        print("No dataset found. Using sample data.")
        return None, None

    return recipes_df, ingredients_df

def preprocess_data(recipes_df, ingredients_df):
    # Clean and preprocess recipes data
    recipes_df = recipes_df.dropna(subset=['name', 'ingredients', 'diet', 'region'])
    recipes_df['ingredients'] = recipes_df['ingredients'].str.lower().str.split(',')
    recipes_df['ingredients'] = recipes_df['ingredients'].apply(lambda x: [i.strip() for i in x])

    # Merge if separate ingredients dataset
    if 'ingredients' not in recipes_df.columns:
        recipes_df = recipes_df.merge(ingredients_df, on='name', how='left')

    # Create ingredient text for vectorization
    recipes_df['ingredient_text'] = recipes_df['ingredients'].apply(lambda x: ' '.join(x))

    # Filter by diet and region if needed
    recipes_df = recipes_df[recipes_df['diet'].isin(['vegetarian', 'non vegetarian'])]
    recipes_df['diet'] = recipes_df['diet'].map({'vegetarian': 'Veg', 'non vegetarian': 'Non-Veg'})

    return recipes_df

if __name__ == '__main__':
    recipes_df, ingredients_df = load_datasets()
    if recipes_df is not None:
        processed_df = preprocess_data(recipes_df, ingredients_df)
        processed_df.to_csv('processed_recipes.csv', index=False)
        print("Data preprocessing complete. Saved to data/processed_recipes.csv")
    else:
        print("Please download the datasets first.")
