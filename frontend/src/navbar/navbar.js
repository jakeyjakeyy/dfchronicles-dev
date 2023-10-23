import React from "react";
import "./navbar.css";
import { useState, useEffect } from "react";
import Login from "./login";
import NavbarItem from "./navbaritems";


function Navbar({token, username, onLogout, onAppSelect, onLogin}) {
    if (!token) {
        return (
            <div className="Nav">
                <h3>Not logged in</h3>
                <Login />
            </div>
        )
    }
        // Refresh tokens. Not needed here but saving for reference //
    // fetch("http://localhost:8000/api/whoami", {
    //     headers: {
    //         Authorization: `JWT ${localStorage.getItem("token")}`
    //     }
    // })
    //     .then((res) => res.json())
    //     .then((data) => {
    //         if (data.code === "token_not_valid") {
    //             localStorage.removeItem("token");
    //             fetch("http://localhost:8000/api/token/refresh", {
    //                 method: "POST",
    //                 headers: {
    //                     "Content-Type": "application/json",
    //                 },
    //                 body: JSON.stringify({ refresh: localStorage.getItem("refresh") }),
    //             })
    //                 .then((res) => res.json())
    //                 .then((data) => {
    //                     localStorage.setItem("token", data.access);
    //                 })
    //                 .catch((err) => {
    //                     console.log(err);
    //                 });
    //         }
    //         if (data.username){
    //             setUsername(data.username);
    //             localStorage.setItem("username", data.username);
    //         }
    //     });
    return (
        <div className="Nav">
            <div>{username}</div>
            <NavbarItem name="Home" onSelect={onAppSelect} />
            <NavbarItem name="Upload" onSelect={onAppSelect} />
            <NavbarItem name="Worlds" onSelect={onAppSelect} />
            <Login onLogin={onLogin} onLogout={onLogout}/>
        </div>
    );
}

export default Navbar;