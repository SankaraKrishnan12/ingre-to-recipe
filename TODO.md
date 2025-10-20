# Ingredient-to-Recipe Web Application TODO

## Project Setup
- [x] Create project directory structure (backend, frontend, ml_models, data)
- [x] Initialize backend with Flask (requirements.txt, app.py)
- [x] Initialize frontend with React (package.json, src/)

## Dataset Preparation
- [x] Download Indian Food Recipe Dataset from Kaggle
- [x] Download Recipe Ingredients Dataset from Kaggle
- [x] Preprocess datasets (clean, merge, handle missing values)

## Machine Learning Implementation
- [x] Implement TF-IDF vectorization for recipes
- [x] Implement Word2Vec embeddings for recipes
- [x] Implement cosine similarity for recommendations
- [x] Train and save ML models
- [x] Create recommendation functions (TF-IDF and Word2Vec based)

## Backend Development
- [x] Set up Flask app with CORS
- [x] Create API endpoints (/recommend, /recipes)
- [x] Load ML models in backend
- [x] Handle ingredient input, filters (region, diet)
- [x] Return recipe recommendations as JSON

## Database Setup
- [x] Set up SQLite database
- [x] Create tables for recipes, ingredients, metadata
- [x] Populate database with processed data

## Frontend Development
- [x] Create React components (IngredientInput, RecipeCard, Filters)
- [x] Implement UI with Tailwind CSS
- [x] Add state management for ingredients and recommendations
- [x] Fetch data from backend API
- [x] Display recipe cards with details

## Integration and Testing
- [ ] Connect frontend to backend API
- [ ] Test full application locally
- [ ] Verify recommendations accuracy
- [ ] Add error handling and loading states

## Deployment
- [x] Prepare for local deployment
- [x] Document setup and run instructions
