import { useState } from 'react';

interface Props {
  onSearch: (results: any) => void;
}

const SearchBar: React.FC<Props> = ({ onSearch }) => {
  const [searchText, setSearchText] = useState('');

  const handleSearch = async () => {
    const response = await fetch(`http://0.0.0.0:80/search/${searchText}`);
    const results = await response.json();
    onSearch(results);
  };

  return (
    <div>
      <input type="text" value={searchText} onChange={(e) => setSearchText(e.target.value)} />
      <button onClick={handleSearch}>Search</button>
    </div>
  );
};

export default SearchBar;
