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