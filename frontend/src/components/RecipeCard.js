import React from 'react';

function RecipeCard({ recipe }) {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <h3 className="text-xl font-semibold mb-2">{recipe.name}</h3>
      <p className="text-gray-600 mb-2">
        <strong>Region:</strong> {recipe.region} | <strong>Diet:</strong> {recipe.diet}
      </p>
      <div className="mb-4">
        <h4 className="font-medium mb-1">Ingredients:</h4>
        <ul className="text-sm text-gray-700 list-disc list-inside">
          {recipe.ingredients.map((ingredient, index) => (
            <li key={index}>{ingredient}</li>
          ))}
        </ul>
      </div>
      <div>
        <h4 className="font-medium mb-1">Instructions:</h4>
        <p className="text-sm text-gray-700">{recipe.instructions}</p>
      </div>
    </div>
  );
}

export default RecipeCard;
