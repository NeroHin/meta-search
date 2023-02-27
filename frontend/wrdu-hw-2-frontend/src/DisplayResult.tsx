import React from 'react';

interface Result {
  title: string[];
  link: string[];
}

interface Props {
  results: Result[];
}

const DisplayResult: React.FC<Props> = ({ results }) => {
  if (!results || results.length === 0) {
    return <p style={{ textAlign: 'center' }}>Please enter some keyword</p>;
  }
  const duckduckgo = results[0];


  const webSearch = results[1];


  const google = results[2];


  return (
    <div style={{ display: 'flex', justifyContent: 'space-between' }}>
      <div style={{ flex: '1', marginRight: '20px' }}>
        <ul>
          <h2>DuckDuckGo</h2>
          {duckduckgo.title.map((title, index) => (
            <li key={index}>
              <a href={duckduckgo.link[index]}>{title}</a>
            </li>
          ))}
        </ul>
      </div>
      <div style={{ flex: '1', marginRight: '20px' }}>
        <ul>
          <h2>Web Search</h2>
          {webSearch.title.map((title, index) => (
            <li key={index}>
              <a href={webSearch.link[index]}>{title}</a>
            </li>
          ))}
        </ul>
      </div>
      <div style={{ flex: '1' }}>
        <ul>
          <h2>Google</h2>
          {google.title.map((title, index) => (
            <li key={index}>
              <a href={google.link[index]}>{title}</a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default DisplayResult;
