import React from "react";
import "./navbar.css";
import { useState, useEffect } from "react";
import Login from "./login";
import NavbarItem from "./navbaritems";

function Navbar({ token, username, onLogout, onAppSelect, onLogin, app }) {
  window.addEventListener("scroll", function () {
    var scrollHeight = document.documentElement.scrollHeight;
    var scrollTop = document.documentElement.scrollTop;
    var clientHeight = document.documentElement.clientHeight;
    var scrollPercent = scrollTop / (scrollHeight - clientHeight);

    var navBorder = document.querySelector(".Nav-Border");
    navBorder.style.height = scrollPercent * 100 + "%";
  });

  useEffect(() => {
    var navBorder = document.querySelector(".Nav-Border");
    navBorder.style.height = "0%";
  }, [app]);

  if (!token) {
    return (
      <div className="Nav">
        <NavbarItem name="Home" onSelect={onAppSelect} />
        <Login onLogin={onLogin} onLogout={onLogout} />
        <Login register={true} onLogin={onLogin} onLogout={onLogout} />
        <div className="Nav-Border"></div>
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
