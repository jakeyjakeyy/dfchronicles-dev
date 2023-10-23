import React from "react";
import "./Navbar.css";

function NavbarItem({ name, onSelect }) {
  const handleClick = () => {
    onSelect(name);
  };

  return (
    <div className="NavItem" onClick={handleClick}>
      <h4>{name}</h4>
    </div>
  );
}

export default NavbarItem;