import { useState } from 'react';
import SearchBar from './SearchBar'
import DisplayResult from './DisplayResult'

function App() {
  const [results, setResults] = useState([]);

  const handleSearch = (searchResults: any) => {
    setResults(searchResults);
  };

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <DisplayResult results={results} />
    </div>
  );
}

export default App;
