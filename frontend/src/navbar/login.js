import React from "react";
import "./navbar.css";
import { useState, useEffect } from "react";
import LoginForm from "./loginform";


function Login({onLogin, onLogout}) {
    const [showLoginForm, setShowLoginForm] = useState(false);
  
  
    const handleLoginClick = () => {
      setShowLoginForm(true);
    };
  
    const handleLoginFormClose = () => {
      setShowLoginForm(false);
    };
    
  
    if (!localStorage.getItem("token")) {
      return (
        <div className="Login">
          <div onClick={handleLoginClick}>Login</div>
          {showLoginForm && <LoginForm onClose={handleLoginFormClose} />}
        </div>
      );
    } else {
      return (
        <div className="Login">
          <div onClick={onLogout}>Logout</div>
        </div>
      );
    }
  }
  
  export default Login;