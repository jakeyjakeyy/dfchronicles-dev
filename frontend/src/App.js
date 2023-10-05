import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('Fetching Data...');
  useEffect(() => {
    fetch('http://localhost:8000/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
  })
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Dope</h1>
        <h3>{message}</h3>
      </header>
    </div>
  );
}

export default App;
