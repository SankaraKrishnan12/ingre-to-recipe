# Ingredient-to-Recipe Web Application

A machine learning-powered web application that recommends Indian recipes based on available ingredients.

## Features

- **Ingredient-based Recipe Recommendations**: Enter your available ingredients and get personalized recipe suggestions.
- **Dual ML Engines**: Uses TF-IDF and Word2Vec for accurate recommendations.
- **Filters**: Filter by region (North, South, East, West, Central) and diet type (Veg/Non-Veg).
- **Responsive UI**: Built with React and Tailwind CSS for a modern, mobile-friendly interface.

## Tech Stack

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, gensim
- **Database**: SQLite
- **Data Processing**: pandas, numpy

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 14+
- pip and npm

### 1. Clone the Repository

```bash
git clone <repository-url>
cd ingredient-to-recipe
```

### 2. Download Datasets

Download the following datasets from Kaggle and place them in the `data/` folder:

- [Indian Food Recipe Dataset](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101)
- [Recipe Ingredients Dataset](https://www.kaggle.com/datasets/nehaprabhavalkar/indian-food-101) (if separate)

Rename the files to:
- `indian_food.csv`
- `indian_food_ingredients.csv` (if applicable)

### 3. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 4. Data Preprocessing

```bash
cd ../data
python preprocess.py
```

### 5. Train ML Models

```bash
cd ../ml_models
python train_models.py
```

### 6. Populate Database

```bash
cd ../backend
python database.py
```

### 7. Run Backend

```bash
python app.py
```

The backend will run on `http://localhost:5000`.

### 8. Frontend Setup

Open a new terminal:

```bash
cd frontend
npm install
npm start
```

The frontend will run on `http://localhost:3000`.

## API Endpoints

- `POST /recommend`: Get recipe recommendations based on ingredients and filters.
  - Body: `{"ingredients": ["chicken", "rice"], "region": "North", "diet": "Non-Veg"}`
- `GET /recipes`: Get all recipes (with optional filters).

## Usage

1. Enter your available ingredients in the input field.
2. Apply filters for region and diet if desired.
3. Click "Get Recommendations" to see suggested recipes.
4. Browse through the recipe cards for details and instructions.

## Project Structure

```
ingredient-to-recipe/
├── backend/
│   ├── app.py              # Flask API
│   ├── database.py         # SQLite database setup
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   └── App.js          # Main app component
│   └── package.json        # Node dependencies
├── ml_models/
│   └── train_models.py     # ML model training
├── data/
│   └── preprocess.py       # Data preprocessing
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.
