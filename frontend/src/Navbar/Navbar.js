import React from "react";
import "./Navbar.css";
import { useState, useEffect } from "react";
import Login from "./Login";


function Navbar() {
    const [message, setMessage] = useState("Fetching Data...");
    useEffect(() => {
        fetch("http://localhost:8000/api/whoami")
            .then((res) => res.json())
            .then((data) => setMessage(data.user));
    });
    return (
        <div className="Nav">
            <h3>{message}</h3>
            <Login />
        </div>
    );
}

export default Navbar;