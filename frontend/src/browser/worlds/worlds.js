import React from "react";
import "./worlds.css";
import { useState, useEffect } from "react";
import GetWorlds from "../../utils/getworlds";
import ListItem from "../listitem";

function Worlds({ onAppSelect, legendsxml, legendsplusxml }) {
  if (!legendsxml || !legendsplusxml) {
    onAppSelect("Upload");
  } else {
    console.log(legendsxml, legendsplusxml);
    const handleClick = (e) => {
      onAppSelect("World");
    };

    return (
      <div className="World">
        <h3>Worlds</h3>
        <div className="ListItems">
          <ListItem
            name={legendsplusxml.children[1].value}
            name2={legendsplusxml.children[0].value}
            onClick={handleClick}
          />
        </div>
      </div>
    );
  }
}

export default Worlds;
