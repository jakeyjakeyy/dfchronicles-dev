import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import LoadObj from "../../utils/loadobject";
import { useState, useEffect } from "react";
import Object from "./object";
import ListItem from "../listitem";

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
        {categoryData.map((data) => (
          <ListItem
            name2={data.name ? data.name : "Unnamed Event"}
            id={data.id}
            onClick={fetchObj}
            name={data.type ? data.type : data.name}
          />
        ))}
        )
      </div>
    );
  }
}

export default Category;
