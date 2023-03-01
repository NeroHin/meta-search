import { useState } from 'react';

interface Props {
  onSearch: (results: any) => void;
}

const url: string = 'http://nero-buslab-docker-desktop.dog-bangus.ts.net:8000'
const api: string = '/search/'
const version: string = '/api/v1'


const SearchBar: React.FC<Props> = ({ onSearch }) => {
  const [searchText, setSearchText] = useState('');

  const handleSearch = async () => {
    const response = await fetch(url + version + api + searchText); //http://0.0.0.0:8000/search/${searchText}
    const results = await response.json();
    onSearch(results);
  };

  function clearSearchResults() {
    setSearchText('');
    onSearch([]);
  };

  return (
    <div>
      <div className='search-bar'>
        <input type="text" value={searchText} onChange={(e) => setSearchText(e.target.value)} />
      </div>
      <div className='search-bar-button'>
        <button onClick={handleSearch} >Search</button>
        <button onClick={clearSearchResults}>Clear</button>
      </div>

    </div>

  );
};

export default SearchBar;
