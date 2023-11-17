import React from "react";
import { useState, useEffect } from "react";
import "./browser.css";
import UploadXMLForm from "./upload/uploadxmlform";
import Worlds from "./worlds/worlds";
import World from "./world/world";
import Generations from "../utils/generations";
import ListItem from "./listitem";
import ViewGen from "./viewgen";
import UserPage from "./userpage/userpage";

function Browser({ app, onAppSelect }) {
  const [id, setId] = useState(null);
  const [legendsxml, setLegendsxml] = useState(null);
  const [legendsplusxml, setLegendsPlusxml] = useState(null);
  const [gens, setGens] = useState(null);

  const handleSelectId = (id) => {
    setId(id);
  };

  useEffect(() => {
    if (app === "Home") {
      Generations().then((result) => {
        setGens(result);
      });
    }
  }, [app]);

  if (app === "Home") {
    if (!gens) {
      return (
        <div className="Browser">
          <h1>Home</h1>
          <div>loading...</div>
        </div>
      );
    }
    return (
      <div className="Browser">
        <h1>Home</h1>
        <div className="ListItemContainer">
          {gens.map((gen) => (
            <ListItem
              key={gen.id}
              id={gen.id}
              name={gen.title}
              name2={gen.generation}
              onClick={() => {
                onAppSelect("ViewGen");
                handleSelectId(gen);
              }}
              ratings={gen.ratings}
            />
          ))}
        </div>
      </div>
    );
  } else if (app === "Upload") {
    return (
      <div className="Browser">
        <UploadXMLForm
          setLegendsxml={setLegendsxml}
          setLegendsPlusxml={setLegendsPlusxml}
          onAppSelect={onAppSelect}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
        />
      </div>
    );
  } else if (app === "Worlds") {
    return (
      <div className="Browser">
        <Worlds
          onAppSelect={onAppSelect}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
        />
      </div>
    );
  } else if (app === "World") {
    return (
      <div className="Browser">
        <World
          id={id}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
          onAppSelect={onAppSelect}
        />
      </div>
    );
  } else if (app === "ViewGen") {
    return (
      <div className="Browser">
        <ViewGen gen={id} />
      </div>
    );
  } else if (app === "User") {
    return (
      <div className="Browser">
        <UserPage />
      </div>
    );
  }
}

export default Browser;
