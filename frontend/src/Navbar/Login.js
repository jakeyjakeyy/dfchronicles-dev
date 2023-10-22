import React from "react";
import "./Navbar.css";
import { useState, useEffect } from "react";
import LoginForm from "./LoginForm";


function Login() {
    const [message, setMessage] = useState("Fetching Data...");
    const [showLoginForm, setShowLoginForm] = useState(false);
  
    useEffect(() => {
      fetch("http://localhost:8000/api/whoami")
        .then((res) => res.json())
        .then((data) => setMessage(data.user));
    }, []);
  
    const handleLoginClick = () => {
      setShowLoginForm(true);
    };
  
    const handleLoginFormClose = () => {
      setShowLoginForm(false);
    };
  
    if (message === "Guest") {
      return (
        <div className="Login">
          <h3 onClick={handleLoginClick}>Login</h3>
          {showLoginForm && <LoginForm onClose={handleLoginFormClose} />}
        </div>
      );
    } else {
      return (
        <div className="Logout">
          <h3>Logout</h3>
        </div>
      );
    }
  }
  
  export default Login;