import React, { useState } from 'react';
import IngredientInput from './components/IngredientInput';
import RecipeCard from './components/RecipeCard';
import Filters from './components/Filters';
import axios from 'axios';

function App() {
  const [ingredients, setIngredients] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [filters, setFilters] = useState({ region: '', diet: '' });
  const [loading, setLoading] = useState(false);

  const handleRecommend = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/recommend', {
        ingredients,
        ...filters
      });
      setRecommendations(response.data.recommendations);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <div className="container mx-auto px-4">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
          Ingredient-to-Recipe Recommender
        </h1>
        <div className="max-w-4xl mx-auto">
          <IngredientInput
            ingredients={ingredients}
            setIngredients={setIngredients}
          />
          <Filters filters={filters} setFilters={setFilters} />
          <button
            onClick={handleRecommend}
            className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-8"
            disabled={loading}
          >
            {loading ? 'Getting Recommendations...' : 'Get Recipe Recommendations'}
          </button>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {recommendations.map((recipe, index) => (
              <RecipeCard key={index} recipe={recipe} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
