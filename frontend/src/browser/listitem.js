import React from "react";
import "./listitem.css";
import { FaStar } from "react-icons/fa";

function ListItem({ name, name2, id, onClick, ratings }) {
  var rating = null;
  if (ratings.length > 0) {
    let totalrating = ratings.reduce((a, b) => a + b, 0);
    rating = totalrating / ratings.length;
  }
  return (
    <div className="ListItem" id={id} key={id} onClick={onClick}>
      <div className="ListItemHeader">
        <div className="ListItemName" id={id} onClick={onClick}>
          {name}
        </div>
        {rating !== null ? (
          <div className="ListItemRating">
            <small>{rating.toFixed(1)}</small>
            <small>
              <FaStar color="gold" />
            </small>
            <small>({ratings.length})</small>
          </div>
        ) : (
          <div className="ListItemRating">
            <small>No ratings yet</small>
          </div>
        )}
      </div>
      <div className="ListItemName2" id={id} onClick={onClick}>
        {name2}
      </div>
    </div>
  );
}

export default ListItem;
