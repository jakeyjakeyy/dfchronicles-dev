import React from "react";
import "./Navbar.css";
import { useState, useEffect } from "react";
import LoginForm from "./LoginForm";


function Login() {
    const [showLoginForm, setShowLoginForm] = useState(false);
  
  
    const handleLoginClick = () => {
      setShowLoginForm(true);
    };
  
    const handleLoginFormClose = () => {
      setShowLoginForm(false);
    };
    
    const handleLogoutClick = () => {
      localStorage.removeItem("token");
      localStorage.removeItem("refresh");
      localStorage.removeItem("username");
      window.location.reload();
    }
  
    if (!localStorage.getItem("token")) {
      return (
        <div className="Login">
          <h5 onClick={handleLoginClick}>Login</h5>
          {showLoginForm && <LoginForm onClose={handleLoginFormClose} />}
        </div>
      );
    } else {
      return (
        <div className="Login">
          <h5 onClick={handleLogoutClick}>Logout</h5>
        </div>
      );
    }
  }
  
  export default Login;