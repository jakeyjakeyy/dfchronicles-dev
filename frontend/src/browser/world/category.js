import React from "react";
import "./world.css";
import { useState, useEffect } from "react";
import Object from "./object";
import ListItem from "../listitem";

function Category({
  category,
  id,
  setcategoryname,
  legendsxml,
  legendsplusxml,
  onAppSelect,
  onSetId,
}) {
  const [app, setApp] = useState("Categories");
  const [categoryName, setCategoryName] = useState("");
  const [subcategory, setSubcategory] = useState("");
  const [obj, setObj] = useState([]);
  var categoryRaw = "";
  var catCount = {};

  if (category === "Historical Event Collections") {
    categoryRaw = "historical_event_collection";
  } else if (category === "Written Contents") {
    categoryRaw = "written_content";
  }

  const fetchObj = (e) => {
    legendsxml.getElementsByTagName(categoryRaw).forEach((data) => {
      data.getElementsByTagName("id").forEach((id) => {
        if (id.value == e.target.id) {
          setObj(data);
        }
      });
    });
    setcategoryname(e.target.id);
    setApp("Object");
  };

  const getCategories = (e) => {
    setSubcategory(e.target.id);
    setApp("Category");
  };

  if (app === "Loading") {
    return (
      <div className="Category">
        <h3>Loading...</h3>
      </div>
    );
  } else if (app === "Object") {
    console.log(obj);
    return (
      <div className="Category">
        <Object
          object={obj}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
          setcategoryname={setcategoryname}
          onAppSelect={onAppSelect}
          onSetId={onSetId}
        />
      </div>
    );
  } else if (app === "Categories") {
    if (categoryRaw === "written_content") {
      setApp("Category");
    } else {
      CountCategoryTypes(legendsxml, legendsplusxml, catCount, categoryRaw);
      if (window.Object.keys(catCount).length === 1) {
        setApp("Category");
      }
      return (
        <div className="Category">
          {window.Object.entries(catCount).map(([key, value]) => (
            <ListItem
              name={key}
              name2={value}
              id={key}
              onClick={getCategories}
            />
          ))}
        </div>
      );
    }
  } else if (app === "Category") {
    if (
      category == "Historical Events" ||
      category == "Historical Event Collections" ||
      category == "Entities/Governments" ||
      category == "Sites" ||
      category == "Structures" ||
      category == "Underground Regions"
    ) {
      var objects = [];
      legendsxml.getElementsByTagName(categoryRaw).forEach((data) => {
        data.getElementsByTagName("type").forEach((type) => {
          if (type.value === subcategory) {
            objects.push(data);
          }
        });
      });
      console.log(objects);
      return (
        <div className="Category">
          {objects.map((data) => {
            var nameElement = data.getElementsByTagName("name")[0];
            var name =
              nameElement && nameElement.value
                ? nameElement.value
                : "Unnamed Event";
            var typeElement = data.getElementsByTagName("type")[0];
            var name2 =
              typeElement && typeElement.value ? typeElement.value : undefined;
            var idElement = data.getElementsByTagName("id")[0];
            var id = idElement && idElement.value ? idElement.value : undefined;
            return (
              <ListItem name={name} id={id} onClick={fetchObj} name2={name2} />
            );
          })}
        </div>
      );
    } else {
      console.log(legendsxml.getElementsByTagName(categoryRaw));
      return (
        <div className="Category">
          {Array.from(legendsxml.getElementsByTagName(categoryRaw)).map(
            (data) => {
              return (
                <ListItem
                  name={data.getElementsByTagName("form")[0].value}
                  name2={data.getElementsByTagName("title")[0]?.value}
                  id={data.getElementsByTagName("id")[0].value}
                  onClick={fetchObj}
                />
              );
            }
          )}
        </div>
      );
    }
  }
}

function CountCategoryTypes(legendsxml, legendsplusxml, catCount, category) {
  // count each category type
  if (category === "historical_event_collection") {
    legendsxml.getElementsByTagName(category).forEach((data) => {
      data.getElementsByTagName("type").forEach((type) => {
        if (catCount[type.value]) {
          catCount[type.value] += 1;
        } else {
          catCount[type.value] = 1;
        }
      });
    });
  }
}

export default Category;
