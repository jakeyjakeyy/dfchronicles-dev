import React from "react";
import "./viewgen.css";
import { FaRegStar, FaStar } from "react-icons/fa";
import { useState, useEffect } from "react";
import Generations from "../utils/generations";

function ViewGen({ gen }) {
  const [favorite, setFavorite] = React.useState(false);

  useEffect(() => {
    // API call to check if favorite
    async function fetchData() {
      const data = await Generations("favoriteQuery", gen.id);
      if (data.message === "Favorite") {
        setFavorite(true);
      } else {
        setFavorite(false);
      }
    }
    fetchData();
  });

  const handleFavoriteClick = () => {
    // API call to set favorite
    async function fetchData() {
      await Generations("favorite", gen.id).then((data) => {
        if (
          data.message === "Favorite added" ||
          data.message === "Favorite removed"
        ) {
          setFavorite(!favorite);
        } else {
          console.log(data);
        }
      });
    }
    fetchData();
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
