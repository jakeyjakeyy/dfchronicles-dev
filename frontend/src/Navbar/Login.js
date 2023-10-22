import React from "react";
import "./Navbar.css";
import { useState, useEffect } from "react";


function Login() {
    const [message, setMessage] = useState("Fetching Data...");
    useEffect(() => {
        fetch("http://localhost:8000/api/whoami")
            .then((res) => res.json())
            .then((data) => setMessage(data.user));
    });

    if (message === "Guest") {
        return (
            <div className="Login">
                <h3>Login</h3>
            </div>
        )
    } else {
        return (
            <div className="Nav">
                <h3>Logout</h3>
            </div>
        );
    };
}

export default Login;