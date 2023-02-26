interface Props {
    results: any;
  }
  
  const DisplayResult: React.FC<Props> = ({ results }) => {
    return (
      <div>
        {results.map((result: any) => (
          <div key={result.id}>{result.title}</div>
        ))}
      </div>
    );
  };
  
  export default DisplayResult;
  