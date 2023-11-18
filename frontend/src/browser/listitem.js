import React from "react";
import "./listitem.css";
import { FaStar } from "react-icons/fa";

function ListItem({ name, name2, id, onClick, ratings, username }) {
  var rating = null;
  if (ratings && ratings.length > 0) {
    let totalrating = 0;
    for (var i = 0; i < ratings.length; i++) {
      totalrating += ratings[i].rating;
    }
    rating = totalrating / ratings.length;
  }
  return (
    <div className="ListItem" id={id} key={id} onClick={onClick}>
      <div className="ListItemHeader">
        <div className="ListItemName" id={id} onClick={onClick}>
          {name}
        </div>
        <div className="ListItemInfo">
          {rating !== null ? (
            <div className="ListItemRating">
              <small>{rating.toFixed(1)}</small>
              <small>
                <FaStar color="gold" />
              </small>
              <small>({ratings.length})</small>
            </div>
          ) : ratings ? (
            <div className="ListItemRating">
              <small>No ratings yet</small>
            </div>
          ) : null}
          {username !== null ? (
            <div className="ListItemUsername">
              <small>by {username}</small>
            </div>
          ) : null}
        </div>
      </div>
      <div className="ListItemName2" id={id} onClick={onClick}>
        {name2}
      </div>
    </div>
  );
}

export default ListItem;
