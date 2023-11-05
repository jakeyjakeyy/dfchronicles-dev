import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import Category from "./category";
import { useState, useEffect } from "react";
import ListItem from "../listitem";

function World({ id, onSetId, onAppSelect }) {
  const [world, setWorld] = useState([]);
  const [category, setCategory] = useState("World");
  const [categoryname, setCategoryName] = useState();
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
  useEffect(() => {
    async function fetchData() {
      const world = await LoadWorld(id);
      setWorld(world);
    }
    fetchData();
  }, [id]);
  const handleClick = () => {
    console.log(category);
    console.log(categoryname);
    if (category === "World") {
      onSetId(null);
      onAppSelect("Worlds");
    } else if (category && categories.includes(category)) {
      setCategory("World");
      setCategoryName();
    }
  };

  const handleCategory = (e) => {
    setCategoryName(e.target.id);
    setCategory(e.target.id);
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
        <h3>{world.name2}</h3>
        <h4>{world.name}</h4>
        <button onClick={handleClick}>Back</button>
        <h3>{categoryname}</h3>
      </div>
      {category === "World" && (
        // <ul className="CategoriesList">
        //   {categories.map((category, index) => (
        //     <li key={index} onClick={handleCategory}>
        //       {category}
        //     </li>
        //   ))}
        // </ul>
        <div className="ListItemsCategories">
          {categories.map((category, index) => (
            <ListItem id={category} name={category} onClick={handleCategory} />
          ))}
        </div>
      )}
      {category !== "World" && (
        <Category
          category={category}
          id={id}
          setcategoryname={setCategoryName}
        />
      )}
    </div>
  );
}

export default World;
