import React from 'react';
import logo from './logo.svg';
import Navbar from './Navbar/Navbar';
import './App.css';


function App() {

  return (
    <div className="App">
      <Navbar />
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1></h1>
        <h3>yo</h3>
      </header>
    </div>
  );
}

export default App;
