import React, { useState } from "react";
import logo from "./logo.svg";
import Navbar from "./navbar/navbar";
import UploadXMLForm from "./browser/upload/uploadxmlform";
import Browser from "./browser/browser";
import "./App.css";
import { FaGithub } from "react-icons/fa";
import { MdOutlineEmail } from "react-icons/md";
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
    window.location.reload();
  };

  const handleAppSelect = (app) => {
    setSelectedApp(app);
  };

  return (
    <div className="App">
      <div className="App-body">
        <Navbar
          token={token}
          username={username}
          onLogout={handleLogout}
          onAppSelect={handleAppSelect}
          onLogin={handleLogin}
          app={selectedApp}
        />
        <Browser app={selectedApp} onAppSelect={handleAppSelect} />
      </div>
      <div className="App-footer">
        <div className="Footer-Github">
          <a href="https://github.com/jakeyjakeyy/dfchronicles">
            <FaGithub color="white" />
          </a>
        </div>
        <div className="Footer-Mail">
          <a href="mailto:jakerichards210@gmail.com">
            <MdOutlineEmail color="white" />
          </a>
        </div>
      </div>
    </div>
  );
}

export default App;
