import React from "react";
import "./navbar.css";
import { useState, useEffect } from "react";
import Login from "./login";
import NavbarItem from "./navbaritems";

function Navbar({ token, username, onLogout, onAppSelect, onLogin }) {
  window.addEventListener("scroll", function () {
    var scrollHeight = document.documentElement.scrollHeight;
    var scrollTop = document.documentElement.scrollTop;
    var clientHeight = document.documentElement.clientHeight;
    var scrollPercent = scrollTop / (scrollHeight - clientHeight);

    var navBorder = document.querySelector(".Nav-Border");
    navBorder.style.height = scrollPercent * 100 + "%";
  });

  if (!token) {
    return (
      <div className="Nav">
        <h3>Not logged in</h3>
        <Login />
      </div>
    );
  }

  return (
    <div className="Nav">
      <NavbarItem name={username} onSelect={onAppSelect} />
      <NavbarItem name="Home" onSelect={onAppSelect} />
      <NavbarItem name="Upload" onSelect={onAppSelect} />
      <NavbarItem name="Worlds" onSelect={onAppSelect} />
      <Login onLogin={onLogin} onLogout={onLogout} />
      <div className="Nav-Border"></div>
    </div>
  );
}

export default Navbar;
