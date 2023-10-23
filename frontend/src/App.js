import React, {useState} from 'react';
import logo from './logo.svg';
import Navbar from './Navbar/Navbar';
import UploadXMLForm from './UploadXMLForm';
import Browser from './Browser/Browser';
import './App.css';


function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  const [username, setUsername] = useState(localStorage.getItem("username"));
  const [selectedApp, setSelectedApp] = useState("Home");

  const handleLogin = (token, username) => {
    localStorage.setItem("token", token);
    localStorage.setItem("username", username);
    setToken(token);
    setUsername(username);
  };

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("refresh");
    localStorage.removeItem("username");
    setToken(null);
    setUsername(null);
  };

  const handleAppSelect = (app) => {
    setSelectedApp(app);
  };

  return (
    <div className="App-header">
      <Navbar
        token={token}
        username={username}
        onLogout={handleLogout}
        onAppSelect={handleAppSelect}
        onLogin={handleLogin}
      />
      <Browser app={selectedApp} />
    </div>
  );
}

export default App;
