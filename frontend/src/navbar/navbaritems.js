import React from "react";
import "./navbar.css";

function NavbarItem({ name, onSelect }) {
  const handleClick = () => {
    let categories = ["Home", "Upload", "Worlds"];
    if (categories.includes(name)) {
      onSelect(name);
    } else {
      onSelect("User");
    }
  };

  return (
    <div className="NavItem" onClick={handleClick}>
      <h4>{name}</h4>
    </div>
  );
}

export default NavbarItem;
