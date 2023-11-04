import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import Category from "./category";
import { useState, useEffect } from "react";

function World({ id, onSetId, onAppSelect }) {
  const [world, setWorld] = useState([]);
  const [category, setCategory] = useState("World");
  const [categoryname, setCategoryName] = useState();
  useEffect(() => {
    async function fetchData() {
      const world = await LoadWorld(id);
      setWorld(world);
    }
    fetchData();
  }, [id]);
  const handleClick = () => {
    if (category === "World") {
      onSetId(null);
      onAppSelect("Worlds");
    } else {
      setCategory("World");
    }
  };

  const handleCategory = (e) => {
    setCategoryName(e.target.innerHTML);
    setCategory(e.target.innerHTML);
  };

  if (!world) {
    return (
      <div className="World">
        <h1>Loading...</h1>
      </div>
    );
  }

  const categories = [
    "Artifacts",
    "Entities/Governments",
    "Populations",
    "Occasions",
    "Historical Eras",
    "Historical Event Collections",
    "Historical Events",
    "Historical Figures",
    "Regions",
    "Sites",
    "Structures",
    "Underground Regions",
    "Written Contents",
    "World Constructions",
    "Landmasses",
    "Mountain Peaks",
    "Plots",
  ];
  // add dieties to categories

  return (
    <div className="World">
      <div className="WorldHeader">
        <h3>{world.name2}</h3>
        <h4>{world.name}</h4>
        <button onClick={handleClick}>Back</button>
        <h3>{categoryname}</h3>
      </div>
      {category === "World" && (
        <ul className="CategoriesList">
          {categories.map((category, index) => (
            <li key={index} onClick={handleCategory}>
              {category}
            </li>
          ))}
        </ul>
      )}
      {category !== "World" && <Category category={category} id={id} />}
    </div>
  );
}

export default World;
