import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import LoadObj from "../../utils/loadobject";
import { useState, useEffect } from "react";
import Object from "./object";

function Category({ category, id, setcategoryname }) {
  const [categoryData, setCategoryData] = useState([]);
  const [app, setApp] = useState("Category");
  const [genobject, setGenObject] = useState([]);
  useEffect(() => {
    async function fetchData() {
      const categoryData = await LoadWorld(id, category);
      setCategoryData(categoryData);
    }
    fetchData();
  }, [id]);

  const fetchObj = (e) => {
    async function fetchData() {
      const obj = await LoadObj(id, category, e.target.id);
      console.log(obj);
      // return obj;
      setGenObject(JSON.stringify(obj));
    }
    fetchData();
    setcategoryname(e.target.id);
    setApp("Object");
  };

  if (!categoryData || categoryData.length === 0) {
    return (
      <div className="Category">
        <h3>Loading...</h3>
      </div>
    );
  }

  if (app === "Object") {
    return (
      <div className="Category">
        <Object object={genobject} />
      </div>
    );
  } else {
    return (
      <div className="Category">
        <ul className="CategoryList">
          {categoryData.map((data) => (
            <li
              key={data.id}
              category={category}
              id={data.id}
              onClick={fetchObj}
            >
              {category === "Artifacts" && `${data.name} | ${data.item_type}`}
              {category === "Entities/Governments" &&
                `${data.race} ${data.type} | ${data.name}`}
              {category === "Populations" &&
                `${data.entity.name} | ${data.race} | ${data.population}`}
              {category === "Occasions" && `${data.name}`}
              {category === "Historical Eras" &&
                `${data.name} | ${data.start_year} - ${data.end_year}`}
              {category === "Historical Event Collections" &&
                `${data.name} | ${data.type}`}
              {category === "Historical Events" && `${data.type}`}
              {category === "Historical Figures" &&
                `${data.name} ${data.race} | ${data.birth_year}`}
              {category === "Regions" && `${data.name} | ${data.type}`}
              {category === "Sites" && `${data.name} | ${data.type}`}
              {category === "Structures" && `${data.name} | ${data.type}`}
              {category === "Underground Regions" &&
                `${data.type} | ${data.depth}`}
              {category === "Written Contents" &&
                `${data.title} | ${data.form}`}
              {category === "World Constructions" &&
                `${data.name} | ${data.type}`}
              {category === "Landmasses" &&
                `${data.name} (${data.coord1})-(${data.coord2})`}
              {category === "Mountain Peaks" &&
                `${data.name} ${data.height} | ${data.volcano}`}
              {category === "Plots" && `${data.type}`}
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default Category;
