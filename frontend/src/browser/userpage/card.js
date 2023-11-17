import React from "react";
import "./card.css";

function Card({ title, number, onClick }) {
  return (
    <div className="Card" onClick={onClick}>
      <div className="Title">{title}</div>
      <div className="Number">{number}</div>
    </div>
  );
}

export default Card;
