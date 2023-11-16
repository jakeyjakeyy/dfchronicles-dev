import React from "react";
import { FaRegStar, FaStar } from "react-icons/fa";

function Rating({ rating, onClick }) {
  const stars = Array.from({ length: 5 }, (_, index) =>
    index < rating ? (
      <FaStar onClick={() => onClick(index + 1)} color="gold" />
    ) : (
      <FaRegStar onClick={() => onClick(index + 1)} color="gold" />
    )
  );
  return <div>{stars}</div>;
}

export default Rating;
