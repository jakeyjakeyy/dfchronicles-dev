import React from "react";
import "./worlds.css";
import { useState, useEffect } from "react";
import GetWorlds from "../../utils/getworlds";

function Worlds({onAppSelect, onSetId}) {
    const handleClick = (e) => {
        onSetId(e.target.id);
        onAppSelect("World");
    }
    const [worlds, setWorlds] = useState([]);
      

    useEffect(() => {
        async function fetchData() {
            const worlds = await GetWorlds();
            if (worlds === "Refreshed token") {
                setWorlds([]);
            } else {
            setWorlds(worlds);
            }
        }
        fetchData();
    }, []);

    return (
        <div className="World">
        <h3>Worlds</h3>
        <ul>
          {worlds.map((world) => (
            <li name={"World"} id={world.id} key={world.id} onClick={handleClick}>{world.name}</li>
          ))}
        </ul>
      </div>
    )
}
    

export default Worlds;