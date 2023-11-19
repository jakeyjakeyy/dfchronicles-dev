import React from "react";
import { FaRegStar, FaStar } from "react-icons/fa";

function Rating({ rating, onClick }) {
  const stars = Array.from({ length: 5 }, (_, index) =>
    index < rating ? (
      <FaStar
        className="RatingStar"
        onClick={() => onClick(index + 1)}
        color="gold"
      />
    ) : (
      <FaRegStar
        className="RatingRegStar"
        onClick={() => onClick(index + 1)}
        color="gold"
      />
    )
  );
  return <div>{stars}</div>;
}

export default Rating;
