import React from 'react';

function Filters({ filters, setFilters }) {
  const regions = ['North', 'South', 'East', 'West', 'Central'];
  const diets = ['Veg', 'Non-Veg'];

  const handleFilterChange = (filterType, value) => {
    setFilters({ ...filters, [filterType]: value });
  };

  return (
    <div className="mb-6">
      <h2 className="text-2xl font-semibold mb-4">Filters</h2>
      <div className="flex flex-wrap gap-4">
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Region
          </label>
          <select
            value={filters.region}
            onChange={(e) => handleFilterChange('region', e.target.value)}
            className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">All Regions</option>
            {regions.map((region) => (
              <option key={region} value={region}>
                {region}
              </option>
            ))}
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-1">
            Diet
          </label>
          <select
            value={filters.diet}
            onChange={(e) => handleFilterChange('diet', e.target.value)}
            className="px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          >
            <option value="">All Diets</option>
            {diets.map((diet) => (
              <option key={diet} value={diet}>
                {diet}
              </option>
            ))}
          </select>
        </div>
      </div>
    </div>
  );
}

export default Filters;
