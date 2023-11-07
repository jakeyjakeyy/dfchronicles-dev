import React from "react";
import "./world.css";
import LoadWorld from "../../utils/loadworld";
import LoadObj from "../../utils/loadobject";
import { useState, useEffect } from "react";
import Object from "./object";
import ListItem from "../listitem";

function Category({ category, id, setcategoryname }) {
  const [categoryData, setCategoryData] = useState([]);
  const [app, setApp] = useState("Loading");
  const [genobject, setGenObject] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const loadeddata = await LoadWorld(id, category);
      setCategoryData(loadeddata);
    }
    fetchData().then(() => {
      setApp("Categories");
    });
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

  const getCategories = (e) => {
    return true;
  };

  if (app === "Loading") {
    return (
      <div className="Category">
        <h3>Loading...</h3>
      </div>
    );
  } else if (app === "Object") {
    return (
      <div className="Category">
        <Object object={genobject} />
      </div>
    );
  } else if (app === "Categories") {
    // count each category type
    var catCount = {};
    categoryData.forEach((data) => {
      if (catCount[data.type]) {
        catCount[data.type] += 1;
      } else {
        catCount[data.type] = 1;
      }
    });
    console.log(catCount);
    return (
      <div className="Category">
        {window.Object.entries(catCount).map(([key, value]) => (
          <ListItem name={key} name2={value} onClick={getCategories} />
        ))}
      </div>
    );
  } else if (app === "Category") {
    return (
      <div className="Category">
        {/* <input
          type="text"
          placeholder="Search..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        /> */}
        {categoryData
          .filter(
            (data) =>
              data.type !== "add hf entity link" &&
              data.type !== "remove hf entity link" &&
              data.type !== "add hf site link" &&
              data.type !== "change hf state"
          )
          .map((data) => (
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
