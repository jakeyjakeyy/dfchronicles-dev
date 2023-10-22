import React from "react";
import "./Navbar.css";
import { useState, useEffect } from "react";
import Login from "./Login";


function Navbar() {
    const [username, setUsername] = useState(localStorage.getItem("username"));
    fetch("http://localhost:8000/api/whoami", {
        headers: {
            Authorization: `JWT ${localStorage.getItem("token")}`
        }
    })
        .then((res) => res.json())
        .then((data) => {
            if (data.code === "token_not_valid") {
                localStorage.removeItem("token");;
                localStorage.removeItem("username");
                fetch("http://localhost:8000/api/token/refresh", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ refresh: localStorage.getItem("refresh") }),
                })
                    .then((res) => res.json())
                    .then((data) => {
                        localStorage.setItem("token", data.access);
                    })
                    .catch((err) => {
                        console.log(err);
                    });
            }
            if (data.username){
                setUsername(data.username);
            }
        });
    return (
        <div className="Nav">
            <h3>{username}</h3>
            <Login />
        </div>
    );
}

export default Navbar;