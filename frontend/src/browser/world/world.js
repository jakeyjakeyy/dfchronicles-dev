import React from "react";
import "./world.css";
import Category from "./category";
import { useState, useEffect } from "react";
import ListItem from "../listitem";

function World({ id, legendsxml, legendsplusxml, onAppSelect, onSetId }) {
  const [world, setWorld] = useState([]);
  const [category, setCategory] = useState("Historical Event Collections");
  const [categoryname, setCategoryName] = useState(
    "Historical Event Collections"
  );

  const handleClick = () => {
    console.log(category);
    console.log(categoryname);
    if (category === "World") {
      onAppSelect("Worlds");
    }
  };

  const handleCategory = (e) => {
    setCategoryName(e.target.innerHTML);
    setCategory(e.target.innerHTML);
  };

  if (!world) {
    return (
      <div className="Category">
        <h1>Loading...</h1>
      </div>
    );
  }

  return (
    <div className="World">
      <div className="WorldHeader">
        <h3>{legendsplusxml.children[1].value}</h3>
        <h4>{legendsplusxml.children[0].value}</h4>
        <div className="BackButton" onClick={handleClick}>
          Back
        </div>
        <h4>{categoryname}</h4>
      </div>
      {category !== "World" && (
        <Category
          category={"Historical Event Collections"}
          id={id}
          setcategoryname={setCategoryName}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
          onAppSelect={onAppSelect}
          onSetId={onSetId}
        />
      )}
    </div>
  );
}

export default World;
