import { useState } from 'react';
import SearchBar from './SearchBar';
import DisplayResult from './DisplayResult';

interface Result {
  title: string[];
  description: string[];
  link: string[];
}

function App() {
  const [results, setResults] = useState<Result[]>([]);

  const handleSearch = (searchResults: any) => {
    const formattedResults = Object.values(searchResults).map((result: any) => ({
      title: result.title,
      description: result.description,
      link: result.link,
    }));
    setResults(formattedResults);
  };
  
  return (
    <div>
      <SearchBar onSearch={handleSearch} />
    <DisplayResult results={results} />
  </div>
  );
}

export default App;
