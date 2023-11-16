import React from "react";
import "./viewgen.css";
import { FaRegStar, FaStar } from "react-icons/fa";

function ViewGen({ gen }) {
  const [favorite, setFavorite] = React.useState(false);

  const handleFavoriteClick = () => {
    setFavorite(!favorite);
    // API call to set favorite
  };
  return (
    <div className="ViewGen">
      <div className="ViewGenHeader">
        <h3>{gen.title}</h3>
        <h4>{gen.user}</h4>
        {!favorite && (
          <FaRegStar
            color={"white"}
            className="FavButton"
            onClick={handleFavoriteClick}
          />
        )}
        {favorite && (
          <FaStar
            color={"gold"}
            className="FavButton"
            onClick={handleFavoriteClick}
          />
        )}
      </div>
      <div className="ViewGenContent" style={{ whiteSpace: "pre-wrap" }}>
        <p>{gen.generation}</p>
      </div>
      <div className="ViewGenComments">
        <h4>Comments</h4>
        <p>Comments go here</p>
      </div>
    </div>
  );
}

export default ViewGen;
