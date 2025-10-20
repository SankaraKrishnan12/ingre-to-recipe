import sqlite3
import pandas as pd
import os

def create_database():
    conn = sqlite3.connect('recipes.db')
    c = conn.cursor()

    # Create recipes table
    c.execute('''CREATE TABLE IF NOT EXISTS recipes
                 (id INTEGER PRIMARY KEY,
                  name TEXT NOT NULL,
                  ingredients TEXT,
                  instructions TEXT,
                  region TEXT,
                  diet TEXT)''')

    conn.commit()
    return conn

def populate_database(conn, recipes_df):
    c = conn.cursor()

    for _, recipe in recipes_df.iterrows():
        ingredients_str = ','.join(recipe['ingredients'])
        c.execute('''INSERT OR REPLACE INTO recipes
                     (name, ingredients, instructions, region, diet)
                     VALUES (?, ?, ?, ?, ?)''',
                  (recipe['name'], ingredients_str, recipe.get('instructions', ''),
                   recipe['region'], recipe['diet']))

    conn.commit()

def get_recipes_from_db(conn, region=None, diet=None):
    c = conn.cursor()
    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if region:
        query += " AND region = ?"
        params.append(region)
    if diet:
        query += " AND diet = ?"
        params.append(diet)

    c.execute(query, params)
    rows = c.fetchall()

    recipes = []
    for row in rows:
        recipes.append({
            'id': row[0],
            'name': row[1],
            'ingredients': row[2].split(','),
            'instructions': row[3],
            'region': row[4],
            'diet': row[5]
        })

    return recipes

if __name__ == '__main__':
    if os.path.exists('../data/sample_recipes.csv'):
        recipes_df = pd.read_csv('../data/sample_recipes.csv')
        recipes_df['ingredients'] = recipes_df['ingredients'].apply(eval)

        conn = create_database()
        populate_database(conn, recipes_df)
        conn.close()
        print("Database created and populated.")
    else:
        print("Processed data not found. Run preprocess.py first.")
