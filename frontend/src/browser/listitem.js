import React from "react";
import "./listitem.css";
import {
  FaStar,
  FaCaretRight,
  FaHeart,
  FaRegCommentDots,
  FaCommentDots,
} from "react-icons/fa";

function ListItem({
  name,
  name2,
  id,
  onClick,
  ratings,
  username,
  favorites,
  comments,
}) {
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
              <small>
                <FaStar color="gold" />
              </small>
              <small>{rating.toFixed(1)}</small>
              <small>({ratings.length})</small>
            </div>
          ) : ratings ? (
            <div className="ListItemRating">
              <FaStar color="gold" />
              <small>No ratings yet</small>
            </div>
          ) : null}
          {favorites !== undefined ? (
            <div className="ListItemFavorites">
              <small>
                <FaHeart color="red" />
              </small>
              <small>{favorites.length}</small>
            </div>
          ) : null}
          {comments !== undefined ? (
            <div className="ListItemComments">
              <small>
                <FaCommentDots />
              </small>
              <small>{comments.length}</small>
            </div>
          ) : null}
          {username !== undefined ? (
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
